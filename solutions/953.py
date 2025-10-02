
def main():
    with open("INPUT.TXT", "r") as f:
        m, n = map(int, f.readline().split())
    
    def find_decomposition(current_m, current_n, start, path):
        if current_m == 0:
            return path
        if current_n * current_m < start * current_m:
            return None
        
        for i in range(start, 2 * current_n * current_n + 1):
            if i < start:
                continue
            if current_m * i < current_n:
                continue
            new_m = current_m * i - current_n
            new_n = current_n * i
            if new_m < 0:
                continue
            gcd_val = gcd(new_m, new_n)
            if gcd_val > 1:
                new_m //= gcd_val
                new_n //= gcd_val
            result = find_decomposition(new_m, new_n, i + 1, path + [i])
            if result is not None:
                return result
        return None
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = find_decomposition(m, n, 2, [])
    with open("OUTPUT.TXT", "w") as f:
        f.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
