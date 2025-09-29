
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    B = int(data[1])
    E = int(data[2])
    
    cards = []
    index = 3
    for i in range(n):
        bi = int(data[index])
        ei = int(data[index+1])
        si = int(data[index+2])
        index += 3
        cards.append((bi, ei, si))
    
    cards.sort(key=lambda x: (x[0], x[1]))
    
    heap = []
    current_end = B
    total_cost = 0
    i = 0
    
    while current_end < E:
        while i < n and cards[i][0] <= current_end:
            heapq.heappush(heap, (-cards[i][1], -cards[i][2], cards[i][1], cards[i][2]))
            i += 1
        
        if not heap:
            break
            
        max_end, neg_cost, end, cost = heapq.heappop(heap)
        max_end = -max_end
        cost = -neg_cost
        
        if max_end <= current_end:
            continue
            
        total_cost += cost
        current_end = max_end
        
    print(total_cost)

if __name__ == "__main__":
    main()
