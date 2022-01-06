Enhanced maxmin 
https://www.ijaiem.org/Volume2Issue4/IJAIEM-2013-04-30-130.pdf

# TL;DR
    - Min Min algorithm
        - First MIN --> Find task Ti from task queue which has minimum execution time
        - Second MIN --> Find the machine Mj that will give minimum completion time for Ti
    - Max Min algorithm
        - First MAX --> Find task Ti from task queue which has maximum execution time
        - Second MIN --> Find the machine Mj that will give minimum completion time for Ti
        - Assign Ti to Mj
        - Remove Ti from tasks queue
        - Remove Mj from machines list


# Requirements
    - Research Paper: improved max min heuristic model for task scheduling in cloud
        - Approach
            - Implement MaxMin Algorithm
            - Implement Improved MaxMinAlgorithm
            - Use dummy data to share comparisons
    
    - Research Paper: load balancing by maxmin algorithm in private cloud environment
        - **prefer since has implemented only one algorithm
        - They have used maxmin algo, and plotted metrics using dummy values
        - Approach
            - Implement improved maxmin and plot the same metrics


# Proposed MaxMin algorithm
Task: T1
Machine: M1
Estimated time when the task T1 will be completed from now on machine M1: ET(T1, M1)
Time from now when machine M1 will be available for processing: Mch(M1)
Estimated execution time for task T1 on M1: MT(T1, M1)

tasks: queue containing tasks
machines: list of machines
mat: mapping (machine -> time) of machines to respective machine availability times

et: 2-dimensional matrix to store estimated time of completion 
(rows: number of tasks, columns: number of machines)
+-------------------+
| et | M1 | M2 | M3 |
+-------------------+
| T1 |    |    |    |
+-------------------+
| T2 |    |    |    |
+-------------------+
| T3 |    |    |    |
+-------------------+

for task in tasks:
    for machine in machines:
        # Compute ET(task, machine)
        et[task][machine] = mat[machine] + task.time
