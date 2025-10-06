
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print("Impossible")
        return
        
    n = int(data[0])
    r = int(data[1])
    items = []
    index = 2
    for i in range(n):
        w = int(data[index])
        d = int(data[index+1])
        index += 2
        items.append((w, d, i+1))
    
    low, high = 0, 10**18
    ans_time = -1
    
    def check(T):
        heap = []
        for i in range(n):
            w, d, idx = items[i]
            if w > T:
                time_needed = (w - T + r - 2) // (r - 1)
                if time_needed > d:
                    return False
                heapq.heappush(heap, (time_needed, d, idx))
            elif w <= T:
                if 0 > d:
                    return False
        time_passed = 0
        while heap:
            time_needed, deadline, idx = heapq.heappop(heap)
            time_passed += 1
            if time_passed > time_needed:
                return False
            if time_passed > deadline:
                return False
        return True
    
    if r == 1:
        max_w = 0
        for w, d, idx in items:
            if w > d:
                print("Impossible")
                return
            if w > max_w:
                max_w = w
        print(f"0 {1}")
        for i in range(1, max_w):
            print(f"{i} {1}")
        return

    left, right = 0, 10**18
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans_time = mid
            right = mid - 1
        else:
            left = mid + 1
            
    if ans_time == -1:
        print("Impossible")
        return
        
    T = ans_time
    events = []
    heap = []
    for i in range(n):
        w, d, idx = items[i]
        if w > T:
            time_needed = (w - T + r - 2) // (r - 1)
            heapq.heappush(heap, (time_needed, d, idx))
        else:
            heapq.heappush(heap, (0, d, idx))
            
    time_slots = []
    current_time = 0
    while heap:
        time_needed, deadline, idx = heapq.heappop(heap)
        if current_time < time_needed:
            current_time = time_needed
        if current_time > deadline:
            print("Impossible")
            return
        time_slots.append((current_time, idx))
        current_time += 1
        
    if len(time_slots) > 100000:
        time_slots = time_slots[:100000]
        
    for t, idx in time_slots:
        print(f"{t} {idx}")

if __name__ == "__main__":
    main()
