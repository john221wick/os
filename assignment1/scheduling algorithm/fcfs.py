def fcfs(processes):
    processes.sort(key = lambda x: x[0])

    ct = 0
    wts = []
    tts = []

    for arrival, burst in processes:
        wt = max(0, ct-arrival)
        ct += burst
        tt = ct-arrival
        wts.append(wt)
        tts.append(tt)
    return wts, tts

# Example usage
processes = [(0, 5), (1, 3), (2, 2), (4, 4)]
waiting_times, turnaround_times = fcfs(processes)
print("Waiting Times:", waiting_times)
print("Turnaround Times:", turnaround_times)