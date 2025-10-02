
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    if n < 3:
        print(0)
        return
        
    k = 1
    while True:
        if k * 2 >= n:
            break
        if (n - k) % (k + 1) == 0:
            print(k)
            return
        k += 1
        
    print(0)

if __name__ == '__main__':
    main()
