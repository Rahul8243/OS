def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print("\nOptimal Page Replacement Algorithm")

    for i, page in enumerate(pages):
        if page not in memory: 
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                future_indices = []
                for mem_page in memory:
                    if mem_page in pages[i+1:]:
                        future_indices.append(pages[i+1:].index(mem_page) + i + 1)
                    else:
                        future_indices.append(float("inf"))  # Not used again
                
             
                replace_index = future_indices.index(max(future_indices))
                memory[replace_index] = page

        display = memory + ["Empty"] * (capacity - len(memory))
        print(f"Page {page}: " + " ".join(str(x) for x in display))

    print("\nTotal Page Faults:", page_faults)

num_pages = int(input("Enter the number of pages: "))
capacity = int(input("Enter the number of frames: "))
print("Enter the page reference string:")
pages = [int(input()) for _ in range(num_pages)]

optimal_page_replacement(pages, capacity)
