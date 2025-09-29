
def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while n > 0:
        result.append(digits[n % base])
        n //= base
    return ''.join(result[::-1])

def is_palindrome(s):
    return s == s[::-1]

def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.read().strip())
    
    bases = []
    for base in range(2, 37):
        representation = to_base(N, base)
        if is_palindrome(representation):
            bases.append(base)
    
    if not bases:
        print("none")
    elif len(bases) == 1:
        print("unique")
        print(bases[0])
    else:
        print("multiple")
        print(" ".join(map(str, bases)))

if __name__ == "__main__":
    main()
