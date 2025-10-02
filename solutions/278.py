
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    
    if i == n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
