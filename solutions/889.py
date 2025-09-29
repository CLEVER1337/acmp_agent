
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    m = int(data[1])
    connections = []
    index = 2
    
    for i in range(m):
        p = int(data[index])
        h = int(data[index + 1])
        index += 2
        connections.append((p, h))
    
    left_edges = {}
    right_edges = {}
    
    for p, h in connections:
        left_edges[p] = h
        right_edges[p + 1] = h
    
    current_pos = k
    direction = 'down'
    
    while True:
        if direction == 'down':
            if current_pos in right_edges:
                direction = 'left'
                current_pos -= 1
            elif current_pos in left_edges:
                direction = 'right'
                current_pos += 1
            else:
                break
        elif direction == 'left':
            if current_pos in right_edges:
                direction = 'down'
            else:
                current_pos -= 1
        elif direction == 'right':
            if current_pos in left_edges:
                direction = 'down'
            else:
                current_pos += 1
    
    print(current_pos)

if __name__ == "__main__":
    main()
