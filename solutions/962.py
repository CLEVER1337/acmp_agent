
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    squares = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        l = int(data[index+2])
        index += 3
        squares.append((x, y, l))
    
    count = 0
    
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            ax, ay, al = squares[a]
            bx, by, bl = squares[b]
            
            dx1 = bx - ax
            dy1 = by - ay
            dl1 = bl - al
            
            for c in range(n):
                if c == a or c == b:
                    continue
                for d in range(n):
                    if d == a or d == b or d == c:
                        continue
                    cx, cy, cl = squares[c]
                    dx, dy, dl = squares[d]
                    
                    dx2 = dx - cx
                    dy2 = dy - cy
                    dl2 = dl - cl
                    
                    if dx1 == dx2 and dy1 == dy2 and dl1 == dl2:
                        count += 1
    
    print(count)

if __name__ == "__main__":
    main()
