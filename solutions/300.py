
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("ALIVE")
        return
        
    rockets = []
    for i in range(4):
        t = int(data[i*2])
        v = int(data[i*2+1])
        rockets.append((t, v))
        
    Tpov = int(data[8])
    D = int(data[9])
    
    times = []
    for i, (t, v) in enumerate(rockets):
        time_to_reach = t + D / v
        times.append((time_to_reach, i))
    
    times.sort(key=lambda x: x[0])
    
    shield_pos = 0
    blocked = 0
    first_rocket_index = times[0][1]
    shield_pos = first_rocket_index
    
    for time, idx in times:
        if shield_pos == idx:
            blocked += 1
        else:
            diff = abs(shield_pos - idx)
            if diff == 2:
                needed_time = 2 * Tpov
            else:
                needed_time = Tpov
                
            prev_time = 0
            for prev in times:
                if prev[1] == shield_pos:
                    prev_time = prev[0]
                    break
                    
            if time - prev_time >= needed_time:
                blocked += 1
                shield_pos = idx
            else:
                break
                
    if blocked == 4:
        print("ALIVE")
    else:
        print(blocked)

if __name__ == "__main__":
    main()
