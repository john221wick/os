# 3. Priority Scheduling

# Algorithm Steps:

# Create a list to store the processes with their arrival times, burst times, and priorities.
# Initialize a variable to store the current time.
# Create a priority queue to store the processes based on their priorities.
# Iterate through the priority queue and execute the process with the highest priority first.
# For each process, increment the current time by the burst time of the process.
# Calculate the waiting time and turnaround time for each process.

import heapq

def priority_scheduling(processes):
    # Create a priority queue based on priorities
    pq = [(priority, burst, arrival) for arrival, burst, priority in processes]
    heapq.heapify(pq)

    current_time = 0
    waiting_times = []
    turnaround_times = []

    while pq:
        priority, burst, arrival = heapq.heappop(pq)
        waiting_time = max(0, current_time - arrival)
        current_time += burst
        turnaround_time = current_time - arrival
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

    return waiting_times, turnaround_times

# Example usage
processes = [(0, 5, 2), (1, 3, 1), (2, 2, 3), (4, 4, 2)]
waiting_times, turnaround_times = priority_scheduling(processes)
print("Waiting Times:", waiting_times)
print("Turnaround Times:", turnaround_times)

import heapq

def priority_scheduling(processes):
    pq = []
    current_time = 0
    waiting_times = []
    turnaround_times = []
    executing_process = None
    executing_burst = 0

    for arrival, burst, priority in sorted(processes):
        while current_time < arrival:
            if executing_process:
                executing_burst -= 1
                if executing_burst == 0:
                    executing_process = None
            current_time += 1

        if executing_process:
            heapq.heappush(pq, (executing_process[0], executing_burst, executing_process[2]))
            executing_process = None

        if pq and priority > pq[0][0]:
            executing_burst, _, _ = heapq.heappop(pq)
            executing_process = (pq[0][0], executing_burst, pq[0][2])
            heapq.heappush(pq, (priority, burst, arrival))
        else:
            if executing_process:
                heapq.heappush(pq, (executing_process[0], executing_burst, executing_process[2]))
            executing_process = (priority, burst, arrival)

    while pq:
        priority, burst, arrival = heapq.heappop(pq)
        waiting_time = max(0, current_time - arrival)
        current_time += burst
        turnaround_time = current_time - arrival
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

    return waiting_times, turnaround_times

# Example usage
processes = [(0, 5, 2), (1, 3, 1), (2, 2, 3), (4, 4, 2)]
waiting_times, turnaround_times = priority_scheduling(processes)
print("Waiting Times:", waiting_times)
print("Turnaround Times:", turnaround_times)