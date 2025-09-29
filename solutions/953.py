
def main():
    with open("INPUT.TXT", "r") as f:
        m, n = map(int, f.read().split())
    
    def dfs(remaining_m, remaining_n, start, path):
        if remaining_m == 0:
            return path
        if remaining_m * start > remaining_n:
            return None
        
        for x in range(start, 2 * remaining_n + 1):
            if remaining_m * x < remaining_n:
                continue
            new_n = remaining_n * x
            new_m = remaining_m * x - remaining_n
            gcd_val = gcd(new_m, new_n)
            new_m //= gcd_val
            new_n //= gcd_val
            result = dfs(new_m, new_n, x + 1, path + [x])
            if result is not None:
                return result
        return None
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = dfs(m, n, 2, [])
    with open("OUTPUT.TXT", "w") as f:
        f.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
