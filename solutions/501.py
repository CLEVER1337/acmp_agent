
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    index = 1
    rectangles = []
    
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1])
        x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4
        rectangles.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    
    x1 = int(data[index]); y1 = int(data[index+1])
    x2 = int(data[index+2]); y2 = int(data[index+3])
    construction = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    
    total_area = 0
    cx1, cy1, cx2, cy2 = construction
    
    for rect in rectangles:
        rx1, ry1, rx2, ry2 = rect
        
        overlap_x1 = max(cx1, rx1)
        overlap_y1 = max(cy1, ry1)
        overlap_x2 = min(cx2, rx2)
        overlap_y2 = min(cy2, ry2)
        
        if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
            width = overlap_x2 - overlap_x1
            height = overlap_y2 - overlap_y1
            total_area += width * height
    
    print(total_area)

if __name__ == "__main__":
    main()
