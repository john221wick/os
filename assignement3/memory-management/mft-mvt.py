# MVT (Multi Variable Partitioning Technique) Algorithm:

# Sort the partitions in ascending order.
# Sort the processes in ascending order.
# Iterate over the processes and for each process, find the first partition that can accommodate it.
# Allocate the process to that partition and reduce the size of the partition by the size of the process.
# Repeat step 3 until all processes have been allocated.
# MFT (Multi Fix Partitioning Technique) Algorithm:

# Sort the partitions in descending order.
# Sort the processes in descending order.
# Iterate over the processes and for each process, find the first partition that can accommodate it.
# Allocate the process to that partition and reduce the size of the partition by the size of the process.
# Repeat step 3 until all processes have been allocated.

def MVT(partitions, processes):
    partitions.sort()
    processes.sort()
    allocation = [-1]*len(processes)
    for i in range(len(processes)):
        for j in range(len(partitions)):
            if processes[i] <= partitions[j]:
                allocation[i] = j
                partitions[j] -= processes[i]
                break
    print("Process No.\tProcess Size\tPartition No.")
    for i in range(len(processes)):
        print(i+1, "\t\t", processes[i], "\t\t", allocation[i]+1)

def MFT(partitions, processes):
    partitions.sort(reverse=True)
    processes.sort(reverse=True)
    allocation = [-1]*len(processes)
    for i in range(len(processes)):
        for j in range(len(partitions)):
            if processes[i] <= partitions[j]:
                allocation[i] = j
                partitions[j] -= processes[i]
                break
    print("Process No.\tProcess Size\tPartition No.")
    for i in range(len(processes)):
        print(i+1, "\t\t", processes[i], "\t\t", allocation[i]+1)

partitions = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("MVT:")
MVT(partitions.copy(), processes.copy())
print("\nMFT:")
MFT(partitions.copy(), processes.copy())