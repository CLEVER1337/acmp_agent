
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    rockets = []
    for i in range(4):
        t = int(data[i*2])
        v = int(data[i*2 + 1])
        rockets.append((t, v))
    
    Tpov = int(data[8])
    D = int(data[9])
    
    arrival_times = []
    for i, (t, v) in enumerate(rockets):
        arrival_time = t + D / v
        arrival_times.append((arrival_time, i))
    
    arrival_times.sort()
    
    shield_pos = arrival_times[0][1]
    blocked = 0
    
    for arrival_time, rocket_idx in arrival_times:
        if rocket_idx == shield_pos:
            blocked += 1
            continue
        
        needed_turns = abs(rocket_idx - shield_pos)
        needed_turns = min(needed_turns, 4 - needed_turns)
        
        if arrival_time >= arrival_times[shield_pos][0] + needed_turns * Tpov:
            blocked += 1
            shield_pos = rocket_idx
        else:
            break
    
    if blocked == 4:
        print("ALIVE")
    else:
        print(blocked)

if __name__ == "__main__":
    main()
