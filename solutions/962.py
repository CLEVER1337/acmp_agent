
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
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                for m in range(n):
                    if m == i or m == j or m == k:
                        continue
                    A = squares[i]
                    B = squares[j]
                    C = squares[k]
                    D = squares[m]
                    
                    ax1, ay1, al = A
                    ax2, ay2 = ax1 + al, ay1 + al
                    
                    bx1, by1, bl = B
                    bx2, by2 = bx1 + bl, by1 + bl
                    
                    cx1, cy1, cl = C
                    cx2, cy2 = cx1 + cl, cy1 + cl
                    
                    dx1, dy1, dl = D
                    dx2, dy2 = dx1 + dl, dy1 + dl
                    
                    diff_x1 = ax1 - cx1
                    diff_y1 = ay1 - cy1
                    
                    valid = True
                    
                    if ax1 < bx1:
                        left_x1 = ax1
                    else:
                        left_x1 = bx1
                    
                    if ax2 > bx2:
                        right_x1 = ax2
                    else:
                        right_x1 = bx2
                    
                    if ay1 < by1:
                        bottom_y1 = ay1
                    else:
                        bottom_y1 = by1
                    
                    if ay2 > by2:
                        top_y1 = ay2
                    else:
                        top_y1 = by2
                    
                    if cx1 < dx1:
                        left_x2 = cx1
                    else:
                        left_x2 = dx1
                    
                    if cx2 > dx2:
                        right_x2 = cx2
                    else:
                        right_x2 = dx2
                    
                    if cy1 < dy1:
                        bottom_y2 = cy1
                    else:
                        bottom_y2 = dy1
                    
                    if cy2 > dy2:
                        top_y2 = cy2
                    else:
                        top_y2 = dy2
                    
                    if (right_x1 - left_x1) != (right_x2 - left_x2) or (top_y1 - bottom_y1) != (top_y2 - bottom_y2):
                        valid = False
                    
                    if valid:
                        count += 1
    
    print(count)

if __name__ == "__main__":
    main()
