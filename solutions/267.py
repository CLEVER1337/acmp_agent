
def main():
    with open("INPUT.TXT", "r") as f:
        N, x, y = map(int, f.readline().split())
    
    if x > y:
        x, y = y, x
    
    left = 0
    right = y * N
    
    def count_copies(t):
        if t < x:
            return 0
        return 1 + (t - x) // x + (t - x) // y
    
    while left < right:
        mid = (left + right) // 2
        if count_copies(mid) >= N:
            right = mid
        else:
            left = mid + 1
            
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(left))

if __name__ == "__main__":
    main()
