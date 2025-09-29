
def main():
    with open('INPUT.TXT', 'r') as f:
        a = f.readline().strip()
        b = f.readline().strip()
    
    n = len(a)
    m = len(b)
    count = 0
    
    if m == 0:
        print(0)
        return
        
    doubled_b = b + b
    
    for i in range(n - m + 1):
        substring = a[i:i+m]
        if substring in doubled_b:
            count += 1
            
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
