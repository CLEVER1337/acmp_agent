
def main():
    with open('INPUT.TXT', 'r') as f:
        w, h = map(int, f.readline().split())
        n = int(f.readline().strip())
        
        canvas = [[False] * w for _ in range(h)]
        
        for _ in range(n):
            x1, y1, x2, y2 = map(int, f.readline().split())
            for y in range(y1, y2):
                for x in range(x1, x2):
                    canvas[y][x] = True
        
        white_area = 0
        for row in canvas:
            white_area += sum(1 for cell in row if not cell)
        
        with open('OUTPUT.TXT', 'w') as out:
            out.write(str(white_area))

if __name__ == "__main__":
    main()
