import threading
import time
import os

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        # Call the parent class constructor
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        """
        The run() method is the entry point for the thread's activity.
        """
        print(f"Thread '{self.name}': starting execution.")
        # Simulate some work
        for i in range(3):
            time.sleep(self.delay)
            print(f"Thread '{self.name}': running task {i+1} of 3.")
        print(f"Thread '{self.name}': finishing execution.")

# Main part of the program
if __name__ == "__main__":
    print("Main thread: starting program.")

    # Create new thread instances
    thread1 = MyThread("Thread-1", 1)
    thread2 = MyThread("Thread-2", 0.5)

    # Start the threads by calling the start() method, which in turn calls run()
    thread1.start()
    thread2.start()

    # Wait for both threads to complete before the main thread finishes
    thread1.join()
    thread2.join()

    print("Main thread: all threads are done. Exiting program.")
