
def main():
    a = input().strip()
    b = input().strip()
    n = len(b)
    if n == 0:
        print(0)
        return
        
    double_b = b + b
    pattern = double_b[:n]
    
    count = 0
    for i in range(len(a) - n + 1):
        substring = a[i:i+n]
        if substring in double_b:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
