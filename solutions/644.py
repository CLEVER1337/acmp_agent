
def main():
    n, k = map(int, input().split())
    
    for _ in range(k):
        next_n = n + bin(n).count('1')
        if next_n <= n:
            break
        n = next_n
    
    print(n)

if __name__ == "__main__":
    main()
