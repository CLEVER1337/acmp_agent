
import sys

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(total_seconds):
    h = total_seconds // 3600
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds %= 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    N, K = map(int, data[0].split())
    processes = []
    
    for i in range(1, N + 1):
        time_str, duration = data[i].split()
        processes.append({
            'arrival': time_to_seconds(time_str),
            'duration': int(duration),
            'remaining': int(duration),
            'start': -1,
            'end': -1,
            'index': i - 1
        })
    
    current_time = 0
    batch = []
    completed = 0
    i = 0
    
    while completed < N:
        while i < N and processes[i]['arrival'] <= current_time:
            batch.append(processes[i])
            i += 1
        
        if not batch:
            if i < N:
                current_time = processes[i]['arrival']
                continue
            else:
                break
        
        process = batch.pop(0)
        
        if process['start'] == -1:
            process['start'] = current_time
        
        quantum = 10
        if len(batch) == 0 and i == N:
            quantum = process['remaining']
        
        time_used = min(quantum, process['remaining'])
        current_time += time_used
        process['remaining'] -= time_used
        
        if process['remaining'] == 0:
            process['end'] = current_time
            completed += 1
        else:
            batch.append(process)
        
        while i < N and processes[i]['arrival'] <= current_time:
            batch.append(processes[i])
            i += 1
    
    results = []
    for p in processes:
        start_time = seconds_to_time(p['start'])
        end_time = seconds_to_time(p['end'])
        results.append(f"{start_time} {end_time}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
