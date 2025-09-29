
def main():
    with open('INPUT.TXT', 'r') as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    if len(s1) != len(s2):
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No\n")
        return
    
    n = len(s1)
    if n == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Yes\n0\n")
        return
    
    doubled = s1 + s1
    pos = doubled.find(s2)
    
    if pos == -1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("No\n")
    else:
        k = n - pos
        with open('OUTPUT.TXT', 'w') as f:
            f.write("Yes\n")
            f.write(f"{k}\n")

if __name__ == "__main__":
    main()
