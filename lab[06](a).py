def fifo_page_replacement(pages, capacity):
    memory = ["Empty"] * capacity   
    page_faults = 0
    index = 0  

    print("FIFO Page Replacement Algorithm")
    
    for page in pages:
        if page not in memory:  # Page fault
            memory[index] = page
            index = (index + 1) % capacity
            page_faults += 1

        print(f"Page: {page} =>", " ".join(str(x) for x in memory))

    print("\nTotal Page Faults:", page_faults)

num_pages = int(input("Enter the number of pages: "))
print("Enter the reference string:")
pages = [int(input()) for _ in range(num_pages)]
capacity = int(input("Enter the number of frames: "))

fifo_page_replacement(pages, capacity)
