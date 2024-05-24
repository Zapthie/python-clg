class Process:
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid, self.arrival, self.burst, self.priority = pid, arrival, burst, priority
        self.remaining, self.start, self.completion = burst, -1, 0

def schedule_fcfs(processes):
    processes.sort(key=lambda x: x.arrival)
    current_time = 0
    for p in processes:
        if current_time < p.arrival: current_time = p.arrival
        p.start, p.completion = current_time, current_time + p.burst
        current_time += p.burst

def schedule_sjf(processes):
    processes.sort(key=lambda x: (x.arrival, x.burst))
    current_time = 0
    for p in processes:
        if current_time < p.arrival: current_time = p.arrival
        p.start, p.completion = current_time, current_time + p.burst
        current_time += p.burst

def schedule_priority(processes):
    processes.sort(key=lambda x: (x.arrival, x.priority))
    current_time = 0
    for p in processes:
        if current_time < p.arrival: current_time = p.arrival
        p.start, p.completion = current_time, current_time + p.burst
        current_time += p.burst

def schedule_rr(processes, quantum):
    current_time, queue, n, completed = 0, [], len(processes), 0
    processes.sort(key=lambda x: x.arrival)
    i = 0
    while completed < n:
        while i < n and processes[i].arrival <= current_time:
            queue.append(processes[i])
            i += 1
        if queue:
            p = queue.pop(0)
            if p.start == -1: p.start = current_time
            exec_time = min(p.remaining, quantum)
            current_time += exec_time
            p.remaining -= exec_time
            if p.remaining == 0:
                p.completion = current_time
                completed += 1
            else:
                queue.append(p)
        else:
            current_time += 1

def calculate_metrics(processes):
    total_waiting, total_turnaround, n = 0, 0, len(processes)
    for p in processes:
        turnaround = p.completion - p.arrival
        waiting = turnaround - p.burst
        total_turnaround += turnaround
        total_waiting += waiting
    return total_waiting / n, total_turnaround / n, max(p.completion for p in processes)

def reset_processes(processes, burst_times):
    for i, p in enumerate(processes):
        p.remaining, p.start, p.completion = burst_times[i], -1, 0

def main():
    burst_times = [6, 8, 7, 3]
    processes = [Process(1, 0, 6, 2), Process(2, 1, 8, 1), Process(3, 2, 7, 3), Process(4, 3, 3, 2)]
    quantum = 4
    algorithms = {
        "FCFS": schedule_fcfs,
        "SJF": schedule_sjf,
        "Priority": schedule_priority,
        "Round Robin": lambda procs: schedule_rr(procs, quantum)
    }
    print(f"{'Algorithm':<12} {'Avg Wait Time':<15} {'Avg Turnaround Time':<20} {'Total Completion Time':<20}")
    for name, algorithm in algorithms.items():
        reset_processes(processes, burst_times)
        algorithm(processes)
        avg_waiting, avg_turnaround, total_completion = calculate_metrics(processes)
        print(f"{name:<12} {avg_waiting:<15.2f} {avg_turnaround:<20.2f} {total_completion:<20.2f}")

if __name__ == "__main__":
    main()
