
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        A = int(data[0])
        B = int(data[1])
        C = int(data[2])
        K = int(data[3])
    
    total_stars = A * 1 + B * 2 + C * 3
    if total_stars < K:
        print(0)
        return
    
    shirts = 0
    stars_needed = K
    
    while stars_needed <= total_stars:
        shirts += 1
        stars_needed += K
    
    print(shirts)

if __name__ == "__main__":
    main()
