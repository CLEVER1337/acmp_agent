
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    processes = []
    index = 2
    for i in range(n):
        h, m, s, t = map(int, data[index:index+4])
        index += 4
        arrival_time = h * 3600 + m * 60 + s
        processes.append((arrival_time, t))
    
    start_times = [0] * n
    end_times = [0] * n
    queue = []
    current_time = processes[0][0]
    proc_index = 0
    batch = []
    
    while proc_index < n or queue or batch:
        while proc_index < n and processes[proc_index][0] <= current_time:
            queue.append((proc_index, processes[proc_index][1]))
            proc_index += 1
        
        if not batch and queue:
            batch_size = min(k, len(queue))
            batch = queue[:batch_size]
            queue = queue[batch_size:]
        
        if batch:
            idx, rem_time = batch[0]
            if rem_time <= 10:
                start_times[idx] = current_time
                current_time += rem_time
                end_times[idx] = current_time
                batch.pop(0)
            else:
                start_times[idx] = current_time
                current_time += 10
                rem_time -= 10
                batch[0] = (idx, rem_time)
                batch.append(batch.pop(0))
        else:
            if proc_index < n:
                current_time = processes[proc_index][0]
            else:
                break
        
        while proc_index < n and processes[proc_index][0] <= current_time:
            queue.append((proc_index, processes[proc_index][1]))
            proc_index += 1
    
    for i in range(n):
        start_sec = start_times[i]
        end_sec = end_times[i]
        
        start_h = start_sec // 3600
        start_sec %= 3600
        start_m = start_sec // 60
        start_s = start_sec % 60
        
        end_h = end_sec // 3600
        end_sec %= 3600
        end_m = end_sec // 60
        end_s = end_sec % 60
        
        print(f"{start_h:02d}:{start_m:02d}:{start_s:02d} {end_h:02d}:{end_m:02d}:{end_s:02d}")

if __name__ == "__main__":
    main()
