# Define a class to represent a process with its attributes
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Time at which the process arrives
        self.burst_time = burst_time  # Time required by the process to complete
        self.start_time = 0  # Time at which the process starts execution
        self.completion_time = 0  # Time at which the process completes execution
        self.turnaround_time = 0  # Total time taken from arrival to completion
        self.waiting_time = 0  # Time the process spends waiting in the ready queue

# Function to calculate the scheduling times for each process
def calculate_times(processes):
    # Sort the processes by their arrival time initially
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0  # Initialize the current time to 0
    completed_processes = 0  # Number of processes completed so far
    n = len(processes)  # Total number of processes

    # Keep track of the start and end times for each process
    while completed_processes < n:
        # Find the process with the smallest burst time from the processes that have arrived
        eligible_processes = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        if not eligible_processes:
            current_time += 1  # If no processes have arrived, increment the current time
            continue
        
        shortest_process = min(eligible_processes, key=lambda x: x.burst_time)
        shortest_process.start_time = current_time  # Start time is the current time
        shortest_process.completion_time = current_time + shortest_process.burst_time  # Calculate completion time
        shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time  # Calculate turnaround time
        shortest_process.waiting_time = shortest_process.start_time - shortest_process.arrival_time  # Calculate waiting time
        current_time += shortest_process.burst_time  # Update current time
        completed_processes += 1  # Increment the count of completed processes

# Function to print the process information in a tabular format
def print_table(processes):
    print("PID\tArrival\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.start_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Main function to create processes, calculate their times, and print the result
def main():
    # List of processes with their PID, arrival time, and burst time
    processes = [
        Process(1, 0, 6),
        Process(2, 2, 8),
        Process(3, 4, 7),
        Process(4, 5, 3),
    ]
    
    # Calculate times for each process
    calculate_times(processes)
    
    # Print the process scheduling result
    print_table(processes)

# Execute the main function
if __name__ == "__main__":
    main()
