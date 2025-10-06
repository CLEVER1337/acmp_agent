
def main():
    with open('INPUT.TXT', 'r') as f:
        x, y = map(int, f.read().split())
    
    a = [0] * (x + 1)
    a[x] = y
    
    for i in range(x - 1, 1, -1):
        a[i] = a[i + 2] - a[i + 1]
    
    for i in range(2, 0, -1):
        a[i] = a[i + 2] - a[i + 1]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{a[1]} {a[2]}")
        
if __name__ == "__main__":
    main()
