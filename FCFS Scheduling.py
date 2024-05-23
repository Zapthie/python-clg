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

# Function to calculate start time, completion time, turnaround time, and waiting time for each process
def calculate_times(processes):
    # Sort the processes by their arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0  # Initialize current time to 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # Wait for the process to arrive if the current time is less than the arrival time
        process.start_time = current_time  # Set the start time to the current time
        process.completion_time = current_time + process.burst_time  # Calculate completion time
        process.turnaround_time = process.completion_time - process.arrival_time  # Calculate turnaround time
        process.waiting_time = process.start_time - process.arrival_time  # Calculate waiting time
        current_time += process.burst_time  # Update current time

# Function to print the process information in a tabular format
def print_table(processes):
    print("PID\tArrival\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.start_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

# Main function to create processes, calculate their times, and print the result
def main():
    # List of processes with their PID, arrival time, and burst time
    processes = [
        Process(1, 0, 4),
        Process(2, 1, 3),
        Process(3, 2, 1),
        Process(4, 3, 2),
    ]
    
    # Calculate times for each process
    calculate_times(processes)
    
    # Print the process scheduling result
    print_table(processes)

# Execute the main function
if __name__ == "__main__":
    main()
