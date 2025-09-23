# Interactive Banker's Algorithm Safety Check

def calculate_need(max_matrix, allocation_matrix, n, m):
    """Compute the Need matrix"""
    need = [[max_matrix[i][j] - allocation_matrix[i][j] for j in range(m)] for i in range(n)]
    return need

def is_safe_state(n, m, available, max_matrix, allocation_matrix):
    """Check if the system is in a safe state"""
    need = calculate_need(max_matrix, allocation_matrix, n, m)
    finish = [False] * n
    safe_sequence = []
    work = available.copy()
    
    while len(safe_sequence) < n:
        allocated_in_this_round = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Simulate allocation and release resources
                for j in range(m):
                    work[j] += allocation_matrix[i][j]
                finish[i] = True
                safe_sequence.append(i)
                allocated_in_this_round = True
        if not allocated_in_this_round:
            return False, [], need
    return True, safe_sequence, need

def main():
    # User input
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))
    
    available = list(map(int, input(f"Enter Available resources ({m} values, space-separated): ").split()))
    
    max_matrix = []
    print("\nEnter Max matrix:")
    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        max_matrix.append(row)
    
    allocation_matrix = []
    print("\nEnter Allocation matrix:")
    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))
        allocation_matrix.append(row)
    
    # Safety check
    safe, safe_sequence, need_matrix = is_safe_state(n, m, available, max_matrix, allocation_matrix)
    
    # Display Need matrix
    print("\nNeed matrix:")
    for row in need_matrix:
        print(' '.join(map(str, row)))
    
    # Display safe/unsafe state
    if safe:
        print("\nSystem is in a safe state.")
        print("Safe sequence:", ' -> '.join(f"P{p}" for p in safe_sequence))
    else:
        print("\nSystem is in an unsafe state, deadlock may occur.")

if __name__ == "__main__":
    main()
