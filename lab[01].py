from multiprocessing import Process, current_process

def child_task(child_msg):
    # Child just prints the message received
    print(f"Child Process (Name={current_process().name}, PID={current_process().pid}): {child_msg}")

def main():
    print("Program started...")

    # Take inputs in parent (since Windows child can't use input())
    parent_msg = input("Parent Process: Enter your welcome message: ")
    child_msg = input("Child Process: Enter your welcome message: ")

    # Create child process and pass the child message
    p = Process(target=child_task, args=(child_msg,), name="ChildProcess")
    p.start()

    # Parent prints its own message
    print(f"Parent Process (Name={current_process().name}, PID={current_process().pid}): {parent_msg}")
    print(f"Child Process created with PID={p.pid}")

    p.join()

if __name__ == "__main__":
    main()
