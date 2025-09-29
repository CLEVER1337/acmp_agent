
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        lengths = list(map(int, f.readline().split()))
    
    total_length = sum(lengths)
    max_side = total_length // 2
    
    dp = [False] * (max_side + 1)
    dp[0] = True
    
    for l in lengths:
        for j in range(max_side, l - 1, -1):
            if dp[j - l]:
                dp[j] = True
    
    best_a = 0
    for a in range(max_side, 0, -1):
        if dp[a]:
            best_a = a
            break
    
    b = total_length - best_a
    area = math.sqrt(best_a * b)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{area:.2f}")

if __name__ == "__main__":
    main()
