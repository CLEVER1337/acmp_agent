
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    n = len(s)
    if len(t) != n:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No\n")
        return
    
    if s == t:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Yes\n0")
        return
    
    doubled = s + s
    found = False
    min_k = n
    
    for k in range(1, n):
        candidate = doubled[k:k+n]
        reversed_prefix = s[k-1::-1] if k > 0 else ""
        if candidate == t:
            found = True
            min_k = min(min_k, k)
    
    if found:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(f"Yes\n{min_k}")
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No\n")

if __name__ == "__main__":
    main()
