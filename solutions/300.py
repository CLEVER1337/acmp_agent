
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.readlines()
    
    rockets = []
    for i in range(4):
        t, v = map(int, data[i].split())
        rockets.append((t, v))
    
    Tpov, D = map(int, data[4].split())
    
    arrival_times = []
    for i in range(4):
        arrival_time = rockets[i][0] + D / rockets[i][1]
        arrival_times.append(arrival_time)
    
    shield_pos = 0
    blocked = 0
    
    events = sorted([(arrival_times[i], i) for i in range(4)])
    
    for event_time, rocket_idx in events:
        required_shield_pos = rocket_idx
        
        if shield_pos == required_shield_pos:
            blocked += 1
            continue
        
        turns_needed = abs(shield_pos - required_shield_pos)
        if turns_needed == 3:
            turns_needed = 1
        
        if event_time >= turns_needed * Tpov:
            shield_pos = required_shield_pos
            blocked += 1
        else:
            break
    
    if blocked == 4:
        print("ALIVE")
    else:
        print(blocked)

if __name__ == "__main__":
    main()
