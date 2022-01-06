# Max Min Algorithm

# ready_time [machine]: 
# given as input, default to 0
# time in which the machine will be done with the previous tasks and be ready to execute new task
# 
# execution_time [task][machine]: 
# given as input, defaults to task.time
# time required for a task to execute completely on a machine
# 
# completion_time [task][machine]: 
# computed as execution_time[task][machine] + ready_time[machine]
# total time from now in which the task execution completes on machine

tasks = ['t1','t2','t3', 't4']
machines = ['m1', 'm2']

ready_time = {'m1': 0, 'm2': 0}

execution_time = {
    't1': {'m1': 1,'m2': 0,},
    't2': {'m1': 1,'m2': 1,},
    't3': {'m1': 1,'m2': 1,},
    't4': {'m1': 1,'m2': 1,},
}

completion_time = {
    't1': {'m1': 0,'m2': 0,},
    't2': {'m1': 0,'m2': 0,},
    't3': {'m1': 0,'m2': 0,},
    't4': {'m1': 0,'m2': 0,},
}

# ------------------+
# Max Min Algorithm |
# ------------------+
# Select task ==> Maximum completion time
# Assign machine ==> Minimum execution time

# prepare task queue
task_queue = []
task_queue.extend(tasks)

while task_queue:
    print(f"Task Queue {task_queue}")
    
    # calculate completion time for available tasks
    for task in task_queue:
        for machine in machines:
            completion_time[task][machine] = execution_time[task][machine] + ready_time[machine]
    
    filtered_completion_time = dict(filter(lambda x: x[0] in task_queue, completion_time.items()))
    
    # selected_task ==> task_max_completion_time
    selected_task = max(filtered_completion_time.items(), key=lambda x: max(x[1].values()))[0]
    print(f"selected_task {selected_task}")
    
    # selected_machine ==> machine_min_task_execution_time
    selected_machine = min(execution_time[selected_task].items(), key=lambda x: x[1])[0]
    print(f"selected_machine {selected_machine}")

    # task "task_max_completion_time" assigned to machine "machine_min_task_execution_time"
    print(f"Task {selected_task} assigned to {selected_machine}")

    # remove task from queue
    task_queue.remove(selected_task)

    # update ready_time for machine
    ready_time[selected_machine] += execution_time[selected_task][selected_machine]
    print(f'Ready time for {selected_machine} updated to {ready_time[selected_machine]}')
    print(f"------")

print(f"------ task-queue-empty ------")


"""
Test Run

+-------+
| INPUT |
+-------+

tasks = ['t1','t2','t3', 't4']
machines = ['m1', 'm2']

ready_time = {'m1': 0, 'm2': 0}

execution_time = {
    't1': {'m1': 1,'m2': 0,},
    't2': {'m1': 1,'m2': 1,},
    't3': {'m1': 1,'m2': 1,},
    't4': {'m1': 1,'m2': 1,},
}

completion_time = {
    't1': {'m1': 0,'m2': 0,},
    't2': {'m1': 0,'m2': 0,},
    't3': {'m1': 0,'m2': 0,},
    't4': {'m1': 0,'m2': 0,},
}

+--------+
| OUTPUT |
+--------+

Task Queue ['t1', 't2', 't3', 't4']
selected_task t1
selected_machine m2
Task t1 assigned to m2
Ready time for m2 updated to 0
------
Task Queue ['t2', 't3', 't4']
selected_task t2
selected_machine m1
Task t2 assigned to m1
Ready time for m1 updated to 1
------
Task Queue ['t3', 't4']
selected_task t3
selected_machine m1
Task t3 assigned to m1
Ready time for m1 updated to 2
------
Task Queue ['t4']
selected_task t4
selected_machine m1
Task t4 assigned to m1
Ready time for m1 updated to 3
------
------ task-queue-empty ------
"""