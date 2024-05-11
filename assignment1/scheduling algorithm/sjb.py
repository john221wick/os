# 2. Shortest Job First (SJF) Scheduling

# Algorithm Steps:

# Create a list to store the processes with their arrival times and burst times.
# Initialize a variable to store the current time.
# Create a priority queue to store the processes based on their burst times.
# Iterate through the priority queue and execute the process with the shortest burst time first.
# For each process, increment the current time by the burst time of the process.
# Calculate the waiting time and turnaround time for each process.

import heapq

def sjf(processes):
    # Create a priority queue based on burst times
    pq = [(burst, arrival) for arrival, burst in processes]
    heapq.heapify(pq)

    current_time = 0
    waiting_times = []
    turnaround_times = []

    while pq:
        burst, arrival = heapq.heappop(pq)
        waiting_time = max(0, current_time - arrival)
        current_time += burst
        turnaround_time = current_time - arrival
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

    return waiting_times, turnaround_times

# Example usage
processes = [(0, 5), (1, 3), (2, 2), (4, 4)]
waiting_times, turnaround_times = sjf(processes)
print("Waiting Times:", waiting_times)
print("Turnaround Times:", turnaround_times)