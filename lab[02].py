# Deadlock Detection using Resource Allocation Graph (RAG)

def is_cyclic_util(v, visited, rec_stack, adj):
    visited[v] = True
    rec_stack[v] = True

    for i in range(len(adj)):
        if adj[v][i]:
            if not visited[i] and is_cyclic_util(i, visited, rec_stack, adj):
                return True
            elif rec_stack[i]:
                return True

    rec_stack[v] = False
    return False

def is_deadlock(adj):
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n

    for node in range(n):
        if not visited[node]:
            if is_cyclic_util(node, visited, rec_stack, adj):
                return True
    return False

# -------------------------------
# Input
# -------------------------------
p = int(input("Enter number of processes: "))
r = int(input("Enter number of resources: "))
n = p + r  # total nodes

# Initialize adjacency matrix
adj = [[0 for _ in range(n)] for _ in range(n)]

e = int(input("Enter number of edges: "))
print("Enter each edge one by one:")

for i in range(e):
    print(f"\nEdge {i+1}:")
    while True:
        type_edge = input("  Enter edge type (0=process->resource, 1=resource->process): ").strip()
        if type_edge in ['0','1']:
            type_edge = int(type_edge)
            break
        print("  Invalid type! Enter 0 or 1.")

    if type_edge == 0:  # process -> resource
        from_node = int(input(f"  Enter process index (0 to {p-1}): "))
        to_node = int(input(f"  Enter resource index (0 to {r-1}): "))
        adj[from_node][p + to_node] = 1
    else:  # resource -> process
        from_node = int(input(f"  Enter resource index (0 to {r-1}): "))
        to_node = int(input(f"  Enter process index (0 to {p-1}): "))
        adj[p + from_node][to_node] = 1

# Print adjacency matrix
print("\nAdjacency Matrix:")
for row in adj:
    print(row)

# -------------------------------
# Check for deadlock
# -------------------------------
if is_deadlock(adj):
    print("\nDeadlock detected!")
else:
    print("\nNo deadlock.")
