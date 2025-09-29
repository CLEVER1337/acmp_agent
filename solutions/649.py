
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    left = 0
    count = [0] * 256
    total = 0
    
    for right in range(n):
        count[ord(s[right])] += 1
        
        while count[ord(s[right])] > k:
            count[ord(s[left])] -= 1
            left += 1
            
        total += right - left + 1
        
    print(total)

if __name__ == "__main__":
    main()
