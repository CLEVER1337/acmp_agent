
def main():
    with open('INPUT.TXT', 'r') as f:
        T1, T2, S1, S2, S = map(int, f.readline().split())
    
    if S1 <= S2:
        if S > 0:
            print("NO")
            return
        else:
            print("0.00")
            return
    
    v1 = S1 / T1
    v2 = S2 / T2
    
    if v1 <= v2:
        if S > 0:
            print("NO")
            return
        else:
            print("0.00")
            return
    
    cycle_distance = S1 - S2
    cycle_time = T1 + T2
    
    if S <= 0:
        print("0.00")
        return
    
    full_cycles = S // cycle_distance
    remaining_distance = S % cycle_distance
    
    if remaining_distance == 0:
        total_time = full_cycles * cycle_time - T2
    else:
        if remaining_distance <= S1:
            time_in_cycle = remaining_distance / v1
            total_time = full_cycles * cycle_time + time_in_cycle
        else:
            forward_time = T1
            backward_distance = remaining_distance - S1
            backward_time = backward_distance / v2
            total_time = full_cycles * cycle_time + T1 + backward_time
    
    print("{:.2f}".format(total_time))

if __name__ == "__main__":
    main()
