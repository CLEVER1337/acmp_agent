
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    total_moves = 0
    boxes = A.copy()
    
    for i in range(n):
        if boxes[i] > 1:
            excess = boxes[i] - 1
            boxes[i] = 1
            boxes[(i + 1) % n] += excess
            total_moves += excess
    
    for i in range(n):
        if boxes[i] > 1:
            excess = boxes[i] - 1
            boxes[i] = 1
            boxes[(i + 1) % n] += excess
            total_moves += excess
    
    print(total_moves)

if __name__ == "__main__":
    main()
