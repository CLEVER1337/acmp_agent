
def convert(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    n = num
    while n > 0:
        result.append(digits[n % base])
        n //= base
    return ''.join(reversed(result)) if result else "0"

def calculate_complexity(s):
    return len(s) + len(set(s))

def find_best_base(num):
    best_base = 2
    best_representation = convert(num, 2)
    best_complexity = calculate_complexity(best_representation)
    
    for base in range(3, 37):
        representation = convert(num, base)
        complexity = calculate_complexity(representation)
        
        if complexity < best_complexity:
            best_complexity = complexity
            best_base = base
            best_representation = representation
        elif complexity == best_complexity and base < best_base:
            best_base = base
            best_representation = representation
    
    return best_base, best_representation

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    results = []
    
    for i in range(1, n + 1):
        num = int(data[i])
        base, representation = find_best_base(num)
        results.append(f"{base} {representation}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
