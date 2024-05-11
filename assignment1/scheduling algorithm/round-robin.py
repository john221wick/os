# 4. Round Robin (RR) Scheduling

# Algorithm Steps:

# Create a list to store the processes with their arrival times and burst times.
# Initialize a variable to store the current time and a time quantum (e.g., 2).
# Create a queue to store the processes.
# Iterate through the queue and execute each process for the time quantum.
# If a process finishes within the time quantum, remove it from the queue.
# If a process does not finish within the time quantum, add it to the end of the queue with the remaining burst time.
# Calculate the waiting time and turnaround time for each process.


def round_robin(processes, time_quantum):
    current_time = 0
    queue = [(burst, arrival) for arrival, burst in processes]
    waiting_times = []
    turnaround_times = []

    while queue:
        burst, arrival = queue.pop(0)
        if burst <= time_quantum:
            current_time += burst
            waiting_time = max(0, current_time - arrival)
            turnaround_time = current_time - arrival
            waiting_times.append(waiting_time)
            turnaround_times.append(turnaround_time)
        else:
            burst -= time_quantum
            current_time += time_quantum
            queue.append((burst, arrival))

    return waiting_times, turnaround_times

# Example usage
processes = [(0, 5), (1, 3), (2, 2), (4, 4)]
time_quantum = 2
waiting_times, turnaround_times = round_robin(processes, time_quantum)
print("Waiting Times:", waiting_times)
print("Turnaround Times:", turnaround_times)