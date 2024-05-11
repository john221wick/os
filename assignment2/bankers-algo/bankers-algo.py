# The algorithm is initialized with the maximum resources that can be allocated, the current allocation, and the available resources.
# It then iterates over the processes, checking if the remaining need of a process can be satisfied with the available resources.
# If it can be satisfied, the resources are allocated to the process and the available resources are updated.
# The process is then marked as finished and the sequence of safe execution is updated.
# This process continues until all processes have been executed safely or a deadlock is detected.


def banker_algorithm(need, max, allocation, available):
    n = len(need)
    m = len(need[0])
    work = list(available)
    finish = [False]*n
    sequence = [0]*n

    for i in range(n):
        sequence[i] = -1

    for k in range(n):
        for i in range(n):
            if finish[i] == False:
                flag = True
                for j in range(m):
                    if need[i][j] > work[j]:
                        flag = False
                        break
                if flag == True:
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    sequence[k] = i
                    break

    print("Safe Sequence: ", sequence)

need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [0, 3, 0]]
max = [[3, 9, 6], [6, 4, 3], [3, 5, 7], [4, 6, 3], [5, 7, 4]]
allocation = [[0, 1, 1], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
available = [0, 0, 0]

for i in range(len(allocation)):
    available[0] += allocation[i][0]
    available[1] += allocation[i][1]
    available[2] += allocation[i][2]

available = [3, 3, 2]

banker_algorithm(need, max, allocation, available)