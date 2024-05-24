class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = -1
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_times(processes, quantum):
    processes.sort(key=lambda x: x.arrival_time)
    current_time, completed, queue = 0, 0, []
    i, n = 0, len(processes)
    
    while completed < n:
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if queue:
            process = queue.pop(0)
            if process.start_time == -1:
                process.start_time = current_time
            exec_time = min(process.remaining_time, quantum)
            current_time += exec_time
            process.remaining_time -= exec_time
            if process.remaining_time == 0:
                process.completion_time = current_time
                process.turnaround_time = current_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed += 1
            else:
                queue.append(process)
        else:
            current_time += 1

def print_table(processes):
    print("PID\tArrival\tBurst\tStart\tCompletion\tTurnaround\tWaiting")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.start_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}")

def main():
    processes = [Process(1, 0, 6), Process(2, 1, 8), Process(3, 2, 7), Process(4, 3, 3)]
    quantum = 4
    calculate_times(processes, quantum)
    print_table(processes)

if __name__ == "__main__":
    main()
