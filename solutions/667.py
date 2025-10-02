
def main():
    with open('INPUT.TXT', 'r') as f:
        N, M, K = map(int, f.readline().split())
    
    if M < 2 and N > 0:
        print(0)
        return
        
    total_people = N + M
    buses = (total_people + K - 1) // K
    
    min_buses_for_children = (N + K - 1) // K
    min_adults_needed = 2 * min_buses_for_children
    
    if M < min_adults_needed:
        print(0)
        return
        
    buses_needed = buses
    while buses_needed > 0:
        max_children_per_bus = K - 2
        if max_children_per_bus <= 0:
            print(0)
            return
            
        total_children_capacity = buses_needed * max_children_per_bus
        if total_children_capacity >= N:
            adults_needed = 2 * buses_needed
            if adults_needed <= M:
                remaining_adults = M - adults_needed
                remaining_people = N + remaining_adults
                if remaining_people <= buses_needed * K:
                    print(buses_needed)
                    return
        buses_needed -= 1
        
    print(0)

if __name__ == '__main__':
    main()
