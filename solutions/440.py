
def main():
    centers = [(0, 0), (25, 0), (50, 0), (75, 0), (100, 0)]
    radius = 10
    hit_targets = set()
    
    for _ in range(5):
        x, y = map(int, input().split())
        for i, (cx, cy) in enumerate(centers):
            distance_squared = (x - cx)**2 + (y - cy)**2
            if distance_squared <= radius**2:
                hit_targets.add(i)
                break
    
    print(len(hit_targets))

if __name__ == "__main__":
    main()
