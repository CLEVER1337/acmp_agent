
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    sheets = []
    for i in range(1, n + 1):
        a, b = map(float, data[i].split())
        sheets.append((a, b, i))
    
    def key_func(x):
        a, b, idx = x
        return a * b
    
    sorted_sheets = sorted(sheets, key=key_func)
    
    left = 0.0
    right = 1e12
    
    for _ in range(100):
        mid = (left + right) / 2.0
        total = 0.0
        possible = True
        
        for a, b, idx in sorted_sheets:
            if total > mid:
                possible = False
                break
            remaining = mid - total
            if remaining * b < a:
                possible = False
                break
            total += a / b
        
        if possible:
            left = mid
        else:
            right = mid
    
    T = (left + right) / 2.0
    
    order = []
    total_a = 0.0
    for a, b, idx in sorted_sheets:
        order.append((total_a / b, idx))
        total_a += a
    
    order.sort(key=lambda x: x[0])
    result_order = [str(idx) for _, idx in order]
    
    print("{:.15f}".format(T))
    print(" ".join(result_order))

if __name__ == "__main__":
    main()
