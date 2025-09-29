
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 1:
        print("NO")
        return
        
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
        
    with open('OUTPUT.TXT', 'w') as f:
        if n == 1:
            f.write("NO")
        else:
            f.write("YES")

if __name__ == '__main__':
    main()
