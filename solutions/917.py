
import math

def main():
    with open("INPUT.TXT", "r") as f:
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
            b = total_length - 2 * a
            if b > 0:
                area = math.sqrt(a * b * a * b) / 4
                if area > best_a:
                    best_a = area
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("{:.2f}".format(best_a))

if __name__ == "__main__":
    main()
