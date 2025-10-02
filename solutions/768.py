
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    stars = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        stars.append((x, y))
    
    star_set = set(stars)
    count = 0
    
    for i in range(n):
        x1, y1 = stars[i]
        for j in range(i + 1, n):
            x2, y2 = stars[j]
            dx = x2 - x1
            dy = y2 - y1
            
            if dx != 0 and dy != 0:
                if (x1, y2) in star_set and (x2, y1) in star_set:
                    count += 1
    
    print(count // 2)

if __name__ == "__main__":
    main()
