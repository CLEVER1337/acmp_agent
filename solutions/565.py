
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
        d = int(data[index + 1])
        index += 2
        items.append((w, d, i + 1))
    
    # Сортируем вещи по времени высыхания на веревке (d_i)
    items.sort(key=lambda x: x[1])
    
    current_time = 0
    heap = []
    result = []
    item_index = 0
    
    while item_index < n or heap:
        # Добавляем все вещи, которые нужно начать сушить до current_time
        while item_index < n and items[item_index][1] <= current_time:
            w, d, idx = items[item_index]
            # Если вещь уже должна была высохнуть, но еще не высохла
            if w > current_time:
                print("Impossible")
                return
            item_index += 1
        
        if heap:
            # Берем вещь с наибольшей потребностью в батарее
            neg_need, w, d, idx = heapq.heappop(heap)
            need = -neg_need
            
            # Вычисляем время сушки на батарее
            time_on_battery = (need + r - 1) // r
            
            if time_on_battery > 0:
                # Проверяем, успеет ли высохнуть
                if current_time + time_on_battery > d:
                    print("Impossible")
                    return
                
                result.append((current_time, idx))
                current_time += time_on_battery
                
                # Обновляем влажность после сушки на батарее
                remaining_moisture = need - time_on_battery * r
                if remaining_moisture > 0:
                    heapq.heappush(heap, (-remaining_moisture, remaining_moisture, d, idx))
            else:
                # Вещь уже почти сухая, можно не ставить на батарею
                pass
                
        elif item_index < n:
            # Переходим к следующему времени, когда нужна батарея
            next_d = items[item_index][1]
            if current_time < next_d:
                current_time = next_d
            else:
                current_time += 1
        else:
            break
            
        # Добавляем новые вещи, которые стали актуальными
        while item_index < n and items[item_index][1] <= current_time:
            w, d, idx = items[item_index]
            # Вычисляем, сколько влаги нужно убрать батареей
            moisture_after_line = w - current_time
            if moisture_after_line > 0:
                heapq.heappush(heap, (-moisture_after_line, moisture_after_line, d, idx))
            item_index += 1
    
    # Проверяем, все ли вещи обработаны
    if len(result) == n or all items processed:
        for time, idx in result:
            if time > 10**9 or idx > 10**9:
                print("Impossible")
                return
        for time, idx in result:
            print(f"{time} {idx}")
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
