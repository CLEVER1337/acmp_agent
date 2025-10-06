
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    if n == 0:
        print("0")
        return
        
    if all(c == '0' for c in s):
        print("0")
        return
        
    if s == '1':
        print("0")
        return
        
    if s == '0':
        print("0")
        return
        
    result = []
    i = 0
    while i < n and s[i] == '0':
        i += 1
        
    if i == n:
        print("0")
        return
        
    s = s[i:]
    n = len(s)
    
    if n == 1:
        print("0")
        return
        
    k = n - 1
    while k >= 0 and s[k] == '0':
        k -= 1
        
    if k < 0:
        print("0")
        return
        
    result = ['1'] * (k + 1)
    for i in range(k + 1, n):
        result.append('0')
        
    print(''.join(result))

if __name__ == "__main__":
    main()
