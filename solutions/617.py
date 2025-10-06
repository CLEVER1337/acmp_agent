
def main():
    import sys
    data = sys.stdin.read().split()
    m = int(data[0])
    n = int(data[1])
    w = int(data[2])
    b = int(data[3])
    
    from math import comb
    
    def count_ways(rows, cols, count):
        if count == 0:
            return 1
        if rows < count or cols < count:
            return 0
        total = 0
        for i in range(count + 1):
            sign = 1 if i % 2 == 0 else -1
            total += sign * comb(rows, i) * comb(rows - i, count - i) * comb(cols, count) * comb(count, i)
        return total
    
    total_ways = 0
    max_rooks = min(m, n)
    for i in range(w, max_rooks + 1):
        for j in range(b, max_rooks + 1):
            if i + j > max_rooks:
                continue
            ways_rows = comb(m, i) * comb(m - i, j)
            ways_cols = comb(n, i) * comb(n - i, j)
            ways_white = count_ways(i, j, w)
            ways_black = count_ways(j, i, b)
            total_ways += ways_rows * ways_cols * ways_white * ways_black
    
    print(total_ways)

if __name__ == "__main__":
    main()
