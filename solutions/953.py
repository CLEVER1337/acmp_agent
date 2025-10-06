
def main():
    import sys
    data = sys.stdin.read().split()
    m = int(data[0])
    n = int(data[1])
    
    def dfs(target, start, path):
        if target == 0:
            return path
        if start > 100000:
            return None
            
        for d in range(start, 100000):
            if target * d < 1:
                continue
            if d <= path[-1] if path else 0:
                continue
                
            num = 1
            denom = d
            new_target_num = target[0] * denom - target[1] * num
            new_target_denom = target[1] * denom
            if new_target_num < 0:
                continue
            if new_target_num == 0:
                new_path = path + [d]
                return new_path
            g = gcd(new_target_num, new_target_denom)
            new_target_num //= g
            new_target_denom //= g
            if new_target_denom > 100000 * new_target_num:
                continue
            res = dfs((new_target_num, new_target_denom), d + 1, path + [d])
            if res is not None:
                return res
        return None
        
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
    result = dfs((m, n), 2, [])
    if result:
        print(' '.join(map(str, result)))
    else:
        print("")

if __name__ == "__main__":
    main()
