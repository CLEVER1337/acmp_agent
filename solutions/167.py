
import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n % 2 == 0:
        total = (n * (n + 2) * (2 * n + 1)) // 8
    else:
        total = ((n + 1) * (2 * n * n + 3 * n - 1)) // 8
    print(total)

if __name__ == "__main__":
    main()
