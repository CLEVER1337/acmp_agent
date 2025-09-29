
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    numbers = list(map(int, data[1:1+n]))
    
    if n == 1:
        print("{:.2f}".format(0.0))
        return
        
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
    
    total_cost = 0.0
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum_ab = a + b
        cost = sum_ab * 0.05
        total_cost += cost
        heapq.heappush(heap, sum_ab)
    
    print("{:.2f}".format(total_cost))

if __name__ == "__main__":
    main()
