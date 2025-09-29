
def main():
    n, k = map(int, input().split())
    
    for _ in range(k):
        n += bin(n).count('1')
        if n > 10**18:
            break
            
    print(n)

if __name__ == "__main__":
    main()
