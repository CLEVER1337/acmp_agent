
import sys

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def to_time(total_seconds):
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    processes = []
    for i in range(1, n + 1):
        parts = data[i].split()
        if len(parts) < 2:
            continue
        time_str = parts[0]
        duration = int(parts[1])
        h, m, s = map(int, time_str.split(':'))
        arrival_time = to_seconds(h, m, s)
        processes.append((arrival_time, duration))
    
    packages = []
    for i in range(0, n, k):
        package = []
        for j in range(k):
            idx = i + j
            if idx < n:
                package.append({
                    'arrival': processes[idx][0],
                    'duration': processes[idx][1],
                    'remaining': processes[idx][1],
                    'start': -1,
                    'end': -1,
                    'completed': False
                })
        packages.append(package)
    
    current_time = 0
    results = []
    
    for package in packages:
        queue = package.copy()
        while queue:
            process = queue.pop(0)
            
            if process['start'] == -1:
                process['start'] = max(current_time, process['arrival'])
                current_time = process['start']
            
            if process['remaining'] <= 10:
                process['end'] = current_time + process['remaining']
                current_time = process['end']
                process['remaining'] = 0
                process['completed'] = True
                results.append((process['start'], process['end']))
            else:
                process['remaining'] -= 10
                current_time += 10
                if process['remaining'] > 0:
                    queue.append(process)
    
    for start, end in results:
        print(f"{to_time(start)} {to_time(end)}")

if __name__ == "__main__":
    main()
