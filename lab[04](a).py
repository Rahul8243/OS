def best_fit(blocks, processes):
    n = len(processes)
    m = len(blocks)

    allocation = [-1] * n 
    fragments = [0] * n   
    block_used = [0] * m  

    for i in range(n):
        best_index = -1
        for j in range(m):
            if blocks[j] >= processes[i]:  
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j

        if best_index != -1: 
            allocation[i] = best_index
            fragments[i] = blocks[best_index] - processes[i]
            blocks[best_index] = processes[i]  
        else:
            allocation[i] = -1  

    print("Process_no: Process_size : Block_no: Block_size: Fragement")
    for i in range(n):
        if allocation[i] != -1:
            print(f"{i} {processes[i]} {allocation[i]} {processes[i] + fragments[i]} {fragments[i]}")
        else:
            print(f"Process {i} could not be allocated.")


# Main program with input
if __name__ == "__main__":
    n_blocks = int(input("Enter the number of blocks:"))
    n_processes = int(input("Enter the number of processes:"))

    blocks = []
    print("Enter the size of the blocks:")
    for i in range(n_blocks):
        size = int(input(f"Block {i}:"))
        blocks.append(size)

    processes = []
    print("Enter the size of the processes :-")
    for i in range(n_processes):
        size = int(input(f"Process {i}:"))
        processes.append(size)

    best_fit(blocks, processes)
