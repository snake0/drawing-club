#!/usr/bin/python3

import math
import random
import statistics
import getopt
import sys
import profile

enable_migration = True
prod_overcommit_ratio = 1.0
non_prod_overcommit_ratio = 1.0
warning_threshold = 1.0
n_machines = 800
n_task_events = 10
n_task_usage = 1
# GiantVM #nodes, default is 4
n_nodes = 4
# in secs
total_time = 60000

# Is it necessary to wait for the incompleted tasks when it's high noon?
enable_completion = False

enable_debug = False
enable_info = False
enable_profile = False
def debug(s):
    if (enable_debug):
        print(s)
def info(s):
    if (enable_info):
        print(s)

# calculate gini coefficient of arr
def gini(arr):
    arr = arr.copy()
    arr.sort()

    total_cpu_util = sum(arr)
    if (total_cpu_util == 0):
        return 0
    # Under a absolute fair circumstance, each CPU should have such cpu_util.
    avg_total_cpu_util = 0
    avg_total_cpu_util = total_cpu_util * 1.0 / len(arr)
    Sa_add_b = (len(arr) * total_cpu_util) / 2
    Sa = 0.0

    cum = 0.0
    for i in range(0, len(arr)):
        cum = cum + arr[i]
        assert (avg_total_cpu_util * (i + 1) - cum) >= -0.01
        Sa = Sa + ((avg_total_cpu_util * (i + 1)) - cum)
    return Sa * 1.0 / (Sa_add_b)

class task:
    # usage: a set of tuple (start, end, cpu_util, max_cpu_util, mem_util)
    def __init__(self, task_id, duration, priority, request, usage):
        self.running_start = 0
        self.task_id = task_id
        self.duration = duration * 1.0
        self.schedule = 0
        self.priority = priority
        self.request = request
        self.usage = usage


#f(x) ^
#     |   CPU usage variance in [start, end)
#     |
#     |
#     |
#     |        t2=m*t1
# max |       *********
#     |       |       |
#     |       |       |
#     |       |       |
#     |       |       |
#     |       |       |
#     |       |       |
#     |    t1 |       | t1
#  c  |--******       ******
#     |----------------------------------->
#     0                                   x
#############################################
    def get_usage(self, timestamp):
        for u in self.usage:
            if (timestamp - (self.schedule - self.running_start) >= u[0] and \
                    timestamp - (self.schedule - self.running_start) < u[1]):

                return u[2]

                start = u[0]
                end = u[1]
                avg = u[2]
                maximum = u[3]

                if (abs(avg - maximum) < 0.000001):
                    return avg
                assert(maximum > avg)

                c = avg/2.0
                m = (2*(avg-c)) / (maximum-avg)

                t1 = (end-start) / (2+m)
                t2 = t1*m

                if (debug):
                    my_avg = ((maximum-c)*m*t1+(m+2)*t1*c)/((m+2)*t1)
                    assert abs(my_avg-avg) < .0000001

                if (timestamp <= start + t1):
                    return c
                elif (timestamp <= start + t1 + t2):
                    return maximum
                else:
                    return c
        return 0
    def get_request(self):
        if (self.priority > 2):
            req = self.request * prod_overcommit_ratio
        else:
            req = self.request * non_prod_overcommit_ratio
        return req
    def get_mem_usage(self, timestamp):
        for u in self.usage:
            if (timestamp - (self.schedule - self.running_start) >= u[0] and timestamp - \
                    (self.schedule - self.running_start) < u[1]):
                return u[4]
        return 0

# Each machine have 0.5 CPU, 0.5 memory
class machine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.tasks = set()
        self.tasks_completion = []
        self.pending = set()
        self.request = 0.0
    def get_usage(self, timestamp):
        total = 0.0
        for t in self.tasks:
            total = total + t.get_usage(timestamp)
        return total
    def add_task(self, task, timestamp, fresh):
        req = task.get_request()
        if (fresh):
            reserve = 0.5 - self.request
            if (reserve > req):
                self.tasks.add(task)
                self.request += req
                task.running_start = timestamp
            else:
                self.pending.add(task)
        else:
            self.tasks.add(task)
            self.request += req
    def remove_task(self, task, timestamp):
        assert task in self.tasks

        self.tasks.remove(task)
        self.request -= task.get_request()

        sched = set()
        for t in self.pending:
            reserve = 0.5 - self.request
            if (reserve > t.get_request()):
                sched.add(t)
                self.request += t.get_request()

        for t in sched:
            t.running_start = timestamp
            self.pending.remove(t)
            self.tasks.add(t)
    def get_request(self):
        return self.request

class scheduler:
    def __init__(self):
        self.machines = []
        self.average = []
        self.gini = []
        self.exceeded_load = []
        for i in range(n_machines):
            self.machines.append(machine(i))
        self.migration_mem = 0.0

        self.rr = 0
    # Random selection
    def schedule(self, timestamp, task):
        if (task.priority > 2):
            req = task.request * prod_overcommit_ratio
        else:
            req = task.request * non_prod_overcommit_ratio

        selected = None

        ### CORE SCHEDULING CODE
        idx = self.rr * 4 + int(random.random() * 4)
        selected = self.machines[idx % len(self.machines)]
        self.rr += 1
        ### END SCHEDULING

        selected.add_task(task, timestamp, True)

        info("Task %s CPU req %f scheduled at Machine #%d (CPU %0.2f%%)" %
                (task.task_id, task.request, selected.machine_id,
                    selected.get_usage(timestamp)/0.5*100))
    def migrate(self, timestamp):
        for m in self.machines:
            this_usage = m.get_usage(timestamp)
            if (this_usage >= 0.5 * warning_threshold):
                mid = m.machine_id
                gid = math.floor(mid / n_nodes)
                selected = None
                selected_usage = this_usage
                for i in range(gid * n_nodes, (gid + 1) * n_nodes):
                    if (self.machines[i].get_usage(timestamp) < selected_usage):
                        selected_usage = self.machines[i].get_usage(timestamp)
                        selected = self.machines[i]
                # This is highest-loaded machine
                if (selected == None):
                    continue
                util_diff = 0.0
                removed = set()
                for t in m.tasks:
                    if (t.priority <= 2 and int(t.task_id)%2==0 and
                            t.request < 0.025):
                        removed.add(t)
                        util_diff = util_diff + t.get_usage(timestamp)
                # Migration is useless
                if (selected_usage + util_diff > this_usage or util_diff >
                        this_usage * 0.8 or util_diff > 0.5 or selected_usage +
                        util_diff > 0.5 * warning_threshold):
                    continue
                # Profit is little
                if (util_diff/0.5*100 < 4):
                    continue
                for t in removed:
                    self.migration_mem = self.migration_mem + \
                            t.get_mem_usage(timestamp)
                    m.remove_task(t, timestamp)
                    selected.add_task(t, timestamp, False)
                debug("Migration from #Machine%d (CPU %0.2f%%) to #Machine%d"
                    "(CPU %0.2f%%) diff %0.2f%% (%d)" % (m.machine_id,
                    this_usage/0.5*100,
                    selected.machine_id,
                    selected_usage/0.5*100, util_diff/0.5*100, len(removed)))
    # return: whether there are any tasks or not
    def process(self, timestamp):
        exist = False
        for m in self.machines:
            removed = set()
            for t in m.tasks:
                exist = True
                if (t.running_start + t.duration <= timestamp):
                    removed.add(t)
                    m.tasks_completion.append(t.duration + (t.running_start -
                        t.schedule))
                    info("Task %s completed at %ds (start %ds duartion %ds)"
                            % (t.task_id, timestamp, t.running_start, t.duration))
            for r in removed:
                m.remove_task(r, timestamp)
        return exist
    def record_and_update_duration(self, timestamp):
        utils = []
        exceeded_load = 0.0
        for m in self.machines:
            u = m.get_usage(timestamp)
            if (u > 0.5):
                for t in m.tasks:
                    if (t.priority<=2):
                        if (u - 0.5 > 0.5):
                            t.duration += 1
                        else:
                            t.duration += (u - 0.5) / 0.5
                utils.append(0.5)
                exceeded_load = exceeded_load + (u - 0.5)
            else:
                utils.append(u)
        self.average.append(statistics.mean(utils))
        # Gini coefficient is scale-independant, so it's okay not to scale.
        self.gini.append(gini(utils))
        self.exceeded_load.append(exceeded_load)
    # (mean, gini, overcommit, duration, memory (in MB))
    # Assume 1 memory unit is 512 GB
    def stat(self):
        mean_task_duration = []
        for m in self.machines:
            if (len(m.tasks_completion) > 0):
                mean_task_duration.append(statistics.mean(m.tasks_completion))
        return (statistics.mean(self.average)/0.5*100,
                statistics.mean(self.gini),
                int(statistics.mean(self.exceeded_load)/0.5*100),
                statistics.mean(mean_task_duration),
                self.migration_mem*512*1024*0.07)

# events: {timestamp : list(task)}
def simulate(events):
    assert n_machines%n_nodes == 0

    timestamps = events.keys()
    max_ts = max(timestamps)
    s = scheduler()
    timestamp = 0
    while timestamp < total_time and timestamp <= max_ts:
        if (not timestamp in timestamps):
            # No tasks are submitted at this time
            if (timestamp % 10 == 0 and enable_migration):
                s.migrate(timestamp)
            s.record_and_update_duration(timestamp)
            timestamp = timestamp + 1
            s.process(timestamp)
            continue

        if (len(events[timestamp]) > 0):
            debug("#Events %d at %ds" % (len(events[timestamp]),
                timestamp))

        for t in events[timestamp]:
            s.schedule(timestamp, t)
        if (enable_migration):
            s.migrate(timestamp)
        s.record_and_update_duration(timestamp)
        timestamp = timestamp + 1
        s.process(timestamp)

    if (enable_completion):
        while True:
            if (enable_migration):
                s.migrate(timestamp)
            s.record_and_update_duration(timestamp)
            timestamp = timestamp + 6
            exist = s.process(timestamp)
            if (not exist):
                break

    result = s.stat()
    # (Enable_migration;prod_overcommit_ratio;non_prod_overcommit_ratio;
    #  average_util;gini;overcommit;duration;bandwidth)
    print(str(enable_migration) + ";%0.2f;%0.2f;%d;%0.2f;%0.3f;%0.2f;%d;%0.2f" %
                (prod_overcommit_ratio, non_prod_overcommit_ratio,
                n_machines, result[0], result[1], result[2]/100, result[3],
                result[4]/timestamp/n_machines*1024*8))

def parse_input():
    linecnt = 0
    events = {}
    # task_event
    # {task_id : list (timestamp, event_type, priority, request)}
    records = {}
    total = 0
    for i in range(0, n_task_events):
        with open("../clusterdata-2011-2/task_events/part-" + \
                str(i).rjust(5, '0') + "-of-00500.csv","r") as fp:
            line = fp.readline()
            while line:
                a = line.split(",")

                if (int(a[0])/1000/1000-600 > total_time):
                    break
                task_id = a[2] + a[3]
                # Submit, schedule, finish
                if (a[5] in {"0", "1", "4"}):
                    if (not task_id in records.keys()):
                        records[task_id] = []
                    if (a[9] == ""):
                        records[task_id].append((int(a[0])/1000/1000-600, a[5],
                            int(a[8]), 0.0))
                    else:
                        records[task_id].append((int(a[0])/1000/1000-600, a[5],
                            int(a[8]), float(a[9])))
                line = fp.readline()
    for tid in records.keys():
        l = records[tid]
        if (l[len(l) - 1][1] == "4" and l[len(l) - 2][1] == "1"):
            assert l[0][1] == "0"
            ts = int(l[0][0])
            # Usage is set in the next step
            req = 0
            for tu in l:
                if (tu[3] > 0.0001):
                    req = tu[3]
            if (not ts in events.keys()):
                events[ts] = set()
            events[ts].add(task(tid, (int(l[len(l) - 1][0]) -
                int(l[len(l) - 2][0])), l[0][2], req, None))
            total = total + 1

    debug("task_events loading completed.")

    # task_usage
    # {task_id : list (start, end, cpu_util, max_cpu_util, mem_util)}
    records = {}
    for i in range(0, n_task_usage):
        with open("../clusterdata-2011-2/task_usage/part-" + \
                    str(i).rjust(5, '0') + "-of-00500.csv","r") as fp:
            line = fp.readline()
            while line:
                a = line.split(",")
                if ((int(a[0])/1000/1000-600 > total_time)):
                    break
                task_id = a[2] + a[3]
                if (not task_id in records.keys()):
                    records[task_id] = []
                records[task_id].append((int(a[0])/1000/1000-600, int(a[1])/1000/1000-600, \
                        float(a[5]), float(a[13]), float(a[7])))
                line = fp.readline()
    for ts in events.keys():
        for t in events[ts]:
            if (not t.task_id in records.keys()):
                continue
            t.usage = records[t.task_id]

    # Some events has no usage_traces
    removed = set()
    for ts in events.keys():
        for t in events[ts]:
            t.schedule = ts
            if (t.usage == None):
                removed.add(t)
    for ts in events.keys():
        l = events[ts]
        for r in removed:
            if r in l:
                l.remove(r)
    removed = set()
    for ts in events.keys():
        if len(events[ts]) == 0:
            removed.add(ts)
    for ts in removed:
        del events[ts]

    debug("task_usage loading completed.")

    return events

if __name__=="__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ['enable_migration=',
            'prod_overcommit_ratio=', 'non_prod_overcommit_ratio=',
            'n_machines=', 'n_nodes='])
    except getopt.GetoptError:
        print("Argument error")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--enable_migration":
            if (arg == "False"):
                enable_migration = False
        elif opt == "--prod_overcommit_ratio":
            prod_overcommit_ratio = float(arg)
        elif opt == "--non_prod_overcommit_ratio":
            non_prod_overcommit_ratio = float(arg)
        elif opt == "--n_machines":
            n_machines = int(arg)
        elif opt == "--n_nodes":
            n_nodes = int(arg)
        else:
            print("Argument error2")
            sys.exit(3)

    events = parse_input()
    if (not enable_profile):
        simulate(events)
    else:
        profile.run("simulate(events)")
