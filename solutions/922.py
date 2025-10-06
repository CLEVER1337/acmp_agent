
def main():
    import sys
    data = sys.stdin.read().split()
    T1 = int(data[0])
    T2 = int(data[1])
    S1 = int(data[2])
    S2 = int(data[3])
    S = int(data[4])
    
    v1 = S1 / T1
    v2 = S2 / T2
    
    if v1 <= v2:
        if S <= S1:
            time = S / v1
            print("{:.2f}".format(time))
        else:
            print("NO")
    else:
        cycle_distance = S1 - S2
        if cycle_distance <= 0:
            print("NO")
            return
            
        full_cycles = (S - S1) // cycle_distance
        if (S - S1) % cycle_distance == 0:
            total_time = full_cycles * (T1 + T2) + T1
        else:
            remaining_distance = S - full_cycles * cycle_distance - S1
            if remaining_distance < 0:
                time = S / v1
                print("{:.2f}".format(time))
                return
                
            if remaining_distance <= S1:
                time = full_cycles * (T1 + T2) + T1 + remaining_distance / v1
            else:
                full_cycles += 1
                remaining_distance = S - full_cycles * cycle_distance
                time = full_cycles * (T1 + T2) + remaining_distance / v1
            print("{:.2f}".format(time))

if __name__ == "__main__":
    main()
