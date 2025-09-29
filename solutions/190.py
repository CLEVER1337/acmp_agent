
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n, k = map(int, f.readline().split())
        arr = list(map(int, f.readline().split()))
    
    used = [False] * (n + 1)
    result = 0
    
    for i in range(k):
        current = arr[i]
        count = 0
        for j in range(1, current):
            if not used[j]:
                count += 1
        
        result += count * math.factorial(n - i - 1) // math.factorial(n - i - k + i)
        used[current] = True
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result + 1))

if __name__ == "__main__":
    main()
