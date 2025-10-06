
import math

def main():
    n = int(input().strip())
    L = list(map(int, input().split()))
    
    total = sum(L)
    half = total / 2.0
    
    dp = [False] * (int(total) + 1)
    dp[0] = True
    
    for length in L:
        for j in range(len(dp) - 1, -1, -1):
            if dp[j] and j + length < len(dp):
                dp[j + length] = True
    
    best_diff = float('inf')
    best_sum = 0
    
    for s in range(len(dp)):
        if dp[s]:
            if abs(s - half) < best_diff:
                best_diff = abs(s - half)
                best_sum = s
    
    a = best_sum
    b = total - best_sum
    
    if a > b:
        a, b = b, a
    
    if a <= 0 or b <= 0:
        print(0.0)
    else:
        area = math.sqrt(a * a - (a * a + b * b - total * total) ** 2 / (4.0 * b * b)) * b / 2.0
        print("{:.10f}".format(area))
