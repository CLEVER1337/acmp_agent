
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(boy_mask, pairs_left):
        if pairs_left == 0:
            return 1
            
        boy_idx = boy_mask.bit_count()
        if boy_idx == n:
            return 0
            
        res = 0
        for girl in range(m):
            if grid[boy_idx][girl] == 'Y' and not (boy_mask & (1 << girl)):
                res += dp(boy_mask | (1 << girl), pairs_left - 1)
                
        res += dp(boy_mask, pairs_left)
        return res
        
    result = dp(0, k)
    print(result)

if __name__ == "__main__":
    main()
