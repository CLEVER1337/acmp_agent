
import heapq

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
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
    
    # Проверяем возможность сушки
    for w, d, idx in items:
        if w > d * r:
            print("Impossible")
            return
    
    # Создаем приоритетную очередь по времени, когда вещь должна высохнуть
    heap = []
    for i, (w, d, idx) in enumerate(items):
        # Вычисляем минимальное время, которое вещь должна провести на батарее
        # x - время на батарее, тогда (d - x) - время на веревке
        # x * r + (d - x) >= w
        # x * (r - 1) >= w - d
        # x >= ceil((w - d) / (r - 1)) если r > 1
        if r == 1:
            time_on_radiator = w
        else:
            time_on_radiator = (w - d + r - 2) // (r - 1)
        
        if time_on_radiator < 0:
            time_on_radiator = 0
        
        heapq.heappush(heap, (time_on_radiator, d, idx))
    
    current_time = 0
    result = []
    
    while heap:
        required_time, d, idx = heapq.heappop(heap)
        
        if required_time > d:
            print("Impossible")
            return
            
        if required_time > current_time:
            current_time = required_time
        
        if current_time > d:
            print("Impossible")
            return
            
        result.append((current_time, idx))
        current_time += 1
        
        if len(result) > 100000:
            break
    
    for time, idx in result:
        print(time, idx)

if __name__ == "__main__":
    main()
