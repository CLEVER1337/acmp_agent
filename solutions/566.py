
def main():
    A, B, C, K = map(int, input().split())
    total_stars = A * 1 + B * 2 + C * 3
    if total_stars < K:
        print(0)
        return
        
    left = 0
    right = A + B + C
    while left < right:
        mid = (left + right + 1) // 2
        needed = mid * K
        available = total_stars
        use_c = min(C, (needed + 2) // 3)
        needed -= use_c * 3
        available -= use_c * 3
        
        if needed <= 0:
            left = mid
            continue
            
        use_b = min(B, (needed + 1) // 2)
        needed -= use_b * 2
        available -= use_b * 2
        
        if needed <= 0:
            left = mid
            continue
            
        use_a = min(A, needed)
        needed -= use_a
        available -= use_a
        
        if needed <= 0:
            left = mid
        else:
            right = mid - 1
            
    print(left)

if __name__ == "__main__":
    main()
