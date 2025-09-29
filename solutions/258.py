
def main():
    with open('INPUT.TXT', 'r') as f:
        K1, M, K2, P2, N2 = map(int, f.read().split())
    
    if N2 > M:
        print(-1, -1)
        return
    
    possible_flats_per_floor = set()
    
    for flats_per_floor in range(1, 1001):
        entrance2 = (K2 - 1) // (flats_per_floor * M) + 1
        floor2 = ((K2 - 1) % (flats_per_floor * M)) // flats_per_floor + 1
        
        if entrance2 == P2 and floor2 == N2:
            possible_flats_per_floor.add(flats_per_floor)
    
    if not possible_flats_per_floor:
        print(-1, -1)
        return
    
    entrances = set()
    floors = set()
    
    for flats_per_floor in possible_flats_per_floor:
        entrance1 = (K1 - 1) // (flats_per_floor * M) + 1
        floor1 = ((K1 - 1) % (flats_per_floor * M)) // flats_per_floor + 1
        
        entrances.add(entrance1)
        floors.add(floor1)
    
    p1 = 0 if len(entrances) > 1 else entrances.pop()
    n1 = 0 if len(floors) > 1 else floors.pop()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{p1} {n1}")

if __name__ == "__main__":
    main()
