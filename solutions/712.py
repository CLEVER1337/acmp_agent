
def main():
    with open('INPUT.TXT', 'r') as f:
        w, h, n = map(int, f.read().split())
    
    left = 1
    right = max(w, h) * n
    
    while left < right:
        mid = (left + right) // 2
        cols = mid // w
        rows = mid // h
        
        if (cols * rows) >= n:
            right = mid
        else:
            left = mid + 1
            
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(left))

if __name__ == '__main__':
    main()
