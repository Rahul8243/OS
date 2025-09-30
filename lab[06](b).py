def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print("\nLRU Page Replacement Algorithm")

    for i, page in enumerate(pages):
        if page not in memory: 
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_index = -1
                lru_last_used = float("inf")
                for mem_page in memory:
                
                    last_used = None
                    for j in range(i - 1, -1, -1):
                        if pages[j] == mem_page:
                            last_used = j
                            break
                    if last_used is None:
                        last_used = -1
                    if last_used < lru_last_used:
                        lru_last_used = last_used
                        lru_index = memory.index(mem_page)

            
                memory[lru_index] = page

        display = memory + ["Empty"] * (capacity - len(memory))
        print(f"Page: {page} =>", " ".join(str(x) for x in display))

    print("\nTotal Page Faults:", page_faults)

# Input handling
capacity = int(input("Enter number of frames: "))
num_pages = int(input("Enter number of pages: "))
print("Enter the page reference sequence:")
pages = [int(input()) for _ in range(num_pages)]

lru_page_replacement(pages, capacity)
