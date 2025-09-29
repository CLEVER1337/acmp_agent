
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    V = int(data[1])
    L = int(data[2])
    
    inspectors = []
    index = 3
    for i in range(N):
        xi = int(data[index])
        ti = int(data[index + 1])
        inspectors.append((xi, ti))
        index += 2
    
    inspectors.sort(key=lambda x: x[0])
    
    total_time = 0.0
    current_pos = 0.0
    
    for xi, ti in inspectors:
        distance = xi - current_pos
        time_to_inspector = distance / (V / 60.0)
        total_time += time_to_inspector
        total_time += ti
        current_pos = xi
    
    distance_to_end = L - current_pos
    time_to_end = distance_to_end / (V / 60.0)
    total_time += time_to_end
    
    print("{:.2f}".format(total_time))

if __name__ == "__main__":
    main()
