
def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    
    if M < 2 and N > 0:
        print(0)
        return
        
    total_people = N + M
    buses = (total_people + K - 1) // K
    
    for b in range(buses, total_people + 1):
        if b == 0:
            continue
            
        adults_per_bus = (M + b - 1) // b
        children_per_bus = (N + b - 1) // b
        
        if children_per_bus > 0 and adults_per_bus < 2:
            continue
            
        if children_per_bus <= K - 2 and adults_per_bus <= K:
            max_children_in_bus = min(K - 2, children_per_bus)
            if max_children_in_bus * b >= N and adults_per_bus * b >= M:
                print(b)
                return
        else:
            total_possible = True
            children_left = N
            adults_left = M
            
            for i in range(b):
                seats_available = K
                adults_needed = 0
                
                if children_left > 0:
                    adults_needed = 2
                    children_in_bus = min(children_left, K - adults_needed)
                    children_left -= children_in_bus
                    seats_available -= children_in_bus
                    adults_in_bus = min(adults_left, seats_available, adults_needed)
                    adults_left -= adults_in_bus
                    seats_available -= adults_in_bus
                else:
                    adults_in_bus = min(adults_left, seats_available)
                    adults_left -= adults_in_bus
                    seats_available -= adults_in_bus
                
                if adults_left < 0 or children_left < 0:
                    total_possible = False
                    break
            
            if total_possible and adults_left == 0 and children_left == 0:
                print(b)
                return
                
    print(0)

if __name__ == "__main__":
    main()
