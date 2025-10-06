
def main():
    K, N, M, D = map(int, input().split())
    total = -1
    for x in range(1, 1000000):
        part1 = x // K
        part2 = x // M
        part3 = x // N
        rest = x - part1 - part2 - part3
        if rest == D:
            if part1 * K <= x and part2 * M <= x and part3 * N <= x:
                total = x
                break
    print(total)
