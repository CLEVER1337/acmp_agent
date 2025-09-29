
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
        idx = last_box - 1
        
        total_to_remove = 0
        current = idx
        while True:
            if initial[current] > 0:
                total_to_remove += 1
                initial[current] -= 1
                current = (current - 1) % n
                if current == idx:
                    break
            else:
                break
        
        initial[idx] += total_to_remove
    
    print(" ".join(map(str, initial)))

if __name__ == "__main__":
    main()
