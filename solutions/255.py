
import math

def main():
    n = int(input().strip())
    if n % 2 == 0:
        a = n // 2
        b = n // 2
        if math.gcd(a, b) == a:
            print(a, b)
        else:
            a = n // 2 - 1
            b = n // 2 + 1
            while math.gcd(a, b) != 1:
                a -= 1
                b += 1
            print(a, b)
    else:
        a = n // 2
        b = n - a
        while math.gcd(a, b) != 1:
            a -= 1
            b += 1
        print(a, b)

if __name__ == "__main__":
    main()
