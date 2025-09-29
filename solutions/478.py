
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    sheets = []
    for i in range(1, n + 1):
        a, b = map(float, data[i].split())
        sheets.append((a, b, i))
    
    def key_func(x):
        a, b, idx = x
        return a * b, a
    
    sheets_sorted = sorted(sheets, key=key_func)
    
    total_time = 0.0
    sum_a = 0.0
    for sheet in sheets_sorted:
        a, b, idx = sheet
        total_time += a
        sum_a += a
    
    current_sum = 0.0
    for i in range(len(sheets_sorted)):
        a, b, idx = sheets_sorted[i]
        current_sum += a
        time_from_b = current_sum * b
        if time_from_b > total_time:
            total_time = time_from_b
    
    order = [str(idx) for a, b, idx in sheets_sorted]
    
    print(f"{total_time:.6f}")
    print(" ".join(order))

if __name__ == "__main__":
    main()
