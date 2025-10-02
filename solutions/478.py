
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    sheets = []
    for i in range(1, n + 1):
        a, b = map(float, data[i].split())
        sheets.append((a, b, i))
    
    def time_for_order(order):
        total_a = 0
        total_b = 0
        for idx in order:
            a, b, _ = sheets[idx - 1]
            total_a += a
            total_b += b
        return min(total_a, total_b)
    
    sorted_sheets = sorted(sheets, key=lambda x: x[0] * x[1], reverse=True)
    best_order = [sheet[2] for sheet in sorted_sheets]
    best_time = time_for_order(best_order)
    
    print("{:.15f}".format(best_time))
    print(" ".join(map(str, best_order)))

if __name__ == "__main__":
    main()
