def first_fit(blocks, processes):
    n_blocks = len(blocks)
    n_processes = len(processes)

    allocation = [-1] * n_processes   
    fragments = [0] * n_processes     

    for i in range(n_processes):  
        for j in range(n_blocks):  
            if blocks[j] >= processes[i]:
                allocation[i] = j
                fragments[i] = blocks[j] - processes[i]
                blocks[j] = processes[i]
                break

    print("Process_no: Process_size : Block_no: Block_size: Fragement")
    for i in range(n_processes):
        if allocation[i] != -1:
            print(f"{i} {processes[i]} {allocation[i]} {processes[i] + fragments[i]} {fragments[i]}")
        else:
            print(f"Process {i} could not be allocated.")

# Main Program
if __name__ == "__main__":
    nb = int(input("Enter the number of memory blocks:"))
    np = int(input("Enter the number of processes:"))

    blocks = []
    print("Enter the size of the memory blocks")
    for i in range(nb):
        size = int(input(f"Block {i}:"))
        blocks.append(size)

    processes = []
    print("Enter the size of the processes")
    for i in range(np):
        size = int(input(f"Process {i}:"))
        processes.append(size)

    first_fit(blocks, processes)
