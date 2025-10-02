
def main():
    n = int(input().strip())
    if n == 1:
        print("10 0")
        return
    
    count = 0
    min_num = float('inf')
    
    def dfs(digits, pos, s, p):
        nonlocal count, min_num
        if pos == n:
            if s == p:
                num = int(''.join(map(str, digits)))
                count += 1
                if num < min_num:
                    min_num = num
            return
        
        start = 1 if pos == 0 else 0
        for d in range(start, 10):
            digits[pos] = d
            dfs(digits, pos + 1, s + d, p * d if p != 0 else d)
    
    digits = [0] * n
    dfs(digits, 0, 0, 1)
    
    print(f"{count} {min_num}")

if __name__ == "__main__":
    main()
