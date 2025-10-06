
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    final_config = list(map(int, data[2:2+n]))
    moves = list(map(int, data[2+n:2+n+m]))
    
    boxes = final_config[:]
    
    for i in range(m-1, -1, -1):
        last_box = moves[i] - 1
        total_balls = boxes[last_box]
        boxes[last_box] = 0
        
        k = total_balls
        current = last_box
        while k > 0:
            current = (current - 1) % n
            boxes[current] += 1
            k -= 1
            
    print(' '.join(map(str, boxes)))

if __name__ == "__main__":
    main()
