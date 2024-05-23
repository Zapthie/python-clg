class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_times(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.start_time - process.arrival_time
        current_time += process.burst_time

def print_table(processes):
    print("PID\tArrival\tBurst\tPriority\tStart\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.priority}\t\t{process.start_time}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

def main():
    processes = [
        Process(1, 0, 6, 2),
        Process(2, 2, 8, 1),
        Process(3, 4, 7, 3),
        Process(4, 5, 3, 2),
    ]
    calculate_times(processes)
    print_table(processes)

if __name__ == "__main__":
    main()
