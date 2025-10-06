
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    events = []
    base_sum = 0
    
    for i in range(n):
        idx = 3 + i * 4
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        d = int(data[idx+3])
        
        base_sum += b
        delta = a - b
        events.append((c, delta, d))
        events.append((d, -delta, c))
    
    events.sort(key=lambda x: (x[0], x[2]))
    
    heap = []
    current_sum = 0
    result = base_sum
    
    for event in events:
        stop, delta, other_stop = event
        if delta > 0:
            heapq.heappush(heap, (delta, other_stop))
            current_sum += delta
            if len(heap) > m:
                min_delta, min_stop = heapq.heappop(heap)
                current_sum -= min_delta
        elif delta < 0:
            abs_delta = -delta
            if heap and heap[0][0] < abs_delta:
                min_delta, min_stop = heapq.heappop(heap)
                current_sum -= min_delta
                heapq.heappush(heap, (abs_delta, other_stop))
                current_sum += abs_delta
        result = max(result, base_sum + current_sum)
    
    print(result)

if __name__ == "__main__":
    main()
