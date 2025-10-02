
def main():
    K, N, M, D = map(int, input().split())
    total = K * N * M * D
    for x in range(1, total + 1):
        if (x % K == 0 and x % N == 0 and x % M == 0):
            part1 = x // K
            part2 = x // N
            part3 = x // M
            if part1 + part2 + part3 + D == x:
                print(x)
                return
    print(-1)

if __name__ == "__main__":
    main()
