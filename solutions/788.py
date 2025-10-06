
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = []
    B = []
    index = 1
    for i in range(n):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        A.append(a)
        B.append(b)
    
    total = 0
    for i in range(n):
        total += A[i] + B[i]
    
    dp_prev = [0] * (n + 1)
    dp_curr = [0] * (n + 1)
    
    for i in range(n-1, -1, -1):
        for j in range(0, n+1):
            if j > n - i:
                continue
            if j == 0:
                take_first = A[i] - B[i] + dp_prev[j]
                take_second = -A[i] + B[i] + dp_prev[j+1] if j+1 <= n else -10**18
                dp_curr[j] = max(take_first, take_second)
            else:
                take_first = A[i] - B[i] + dp_prev[j-1] if j-1 >= 0 else -10**18
                take_second = -A[i] + B[i] + dp_prev[j+1] if j+1 <= n else -10**18
                dp_curr[j] = max(take_first, take_second)
        dp_prev, dp_curr = dp_curr, dp_prev
    
    print(dp_prev[0])

if __name__ == "__main__":
    main()
