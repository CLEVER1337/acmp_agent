
def main():
    with open("INPUT.TXT", "r") as f:
        x1, y1 = map(int, f.readline().split())
        x2, y2 = map(int, f.readline().split())
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    if dx == 0 and dy == 0:
        print(0)
        return
    
    if (dx + dy) % 2 != 0:
        print(0)
        return
    
    if dx == dy:
        print(1)
        return
    
    if dx % 2 == dy % 2:
        print(2)
    else:
        print(0)

if __name__ == "__main__":
    main()
