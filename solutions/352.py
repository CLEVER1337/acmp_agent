
import math

def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.read().strip())
    
    if N % 2 == 1:
        numerator = N // 2
        denominator = N - numerator
        if math.gcd(numerator, denominator) == 1:
            print(f"{numerator} {denominator}")
        else:
            print(f"{numerator - 1} {denominator + 1}")
    else:
        half = N // 2
        for i in range(half - 1, 0, -1):
            numerator = i
            denominator = N - i
            if math.gcd(numerator, denominator) == 1:
                print(f"{numerator} {denominator}")
                return

if __name__ == "__main__":
    main()
