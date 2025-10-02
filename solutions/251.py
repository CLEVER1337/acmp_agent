
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    final_config = list(map(int, data[2:2+n]))
    moves = list(map(int, data[2+n:2+n+m]))
    
    initial = final_config[:]
    
    for move_idx in range(m-1, -1, -1):
        last_box = moves[move_idx]
        total_balls = sum(initial)
        idx = (last_box - 1) % n
        
        balls_to_distribute = initial[idx]
        initial[idx] = 0
        
        if balls_to_distribute == 0:
            continue
            
        full_cycles = balls_to_distribute // n
        remainder = balls_to_distribute % n
        
        for i in range(n):
            initial[i] += full_cycles
            
        current = (idx) % n
        for _ in range(remainder):
            current = (current - 1) % n
            initial[current] += 1
            
    print(' '.join(map(str, initial)))

if __name__ == "__main__":
    main()
