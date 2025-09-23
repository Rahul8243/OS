def fixed_partitioning(block_size, n_blocks, processes):
    allocation = [-1] * len(processes)
    fragments = [0] * len(processes)

    for i in range(len(processes)):
        if i < n_blocks:  
            if processes[i] <= block_size:
                allocation[i] = i
                fragments[i] = block_size - processes[i]
            else:
                allocation[i] = -1
        else:
            allocation[i] = -1

    print("Process_no: Process_size : Block_no: Block_size: Fragement")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i} {processes[i]} {allocation[i]} {block_size} {fragments[i]}")
        else:
            print(f"Process {i} could not be allocated.")

if __name__ == "__main__":
    n_blocks = int(input("Enter the number of memory blocks:"))
    block_size = int(input("Enter the size of each memory block:"))

    n_processes = int(input("Enter the number of processes:"))
    processes = []
    print("Enter the size of the processes")
    for i in range(n_processes):
        size = int(input(f"Process {i}:"))
        processes.append(size)

    fixed_partitioning(block_size, n_blocks, processes)
