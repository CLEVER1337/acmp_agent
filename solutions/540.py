
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    first_row = list(map(int, data[3:3+m]))
    
    if n == 1:
        print(" ".join(map(str, first_row)))
        return
        
    dp_prev = first_row[:]
    dp_curr = [0] * m
    
    for i in range(1, n):
        prefix_sum = 0
        for j in range(m):
            prefix_sum = (prefix_sum + dp_prev[j]) % r
            dp_curr[j] = prefix_sum
        
        dp_prev, dp_curr = dp_curr, dp_prev
    
    print(" ".join(map(str, dp_prev)))

if __name__ == "__main__":
    main()
