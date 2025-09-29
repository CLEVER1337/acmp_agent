
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    fractions = []
    for denominator in range(2, N + 1):
        for numerator in range(1, denominator):
            if math.gcd(numerator, denominator) == 1:
                fractions.append((numerator / denominator, f"{numerator}/{denominator}"))
    
    fractions.sort(key=lambda x: x[0])
    
    with open('OUTPUT.TXT', 'w') as f:
        for fraction in fractions:
            f.write(fraction[1] + '\n')

if __name__ == "__main__":
    main()
