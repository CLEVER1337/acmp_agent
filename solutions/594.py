
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    conversion = {
        'm': 1,
        'km': 1000,
        'mile': 1609,
        'uin': 33,
        'kairi': 1852,
        'zhang': 3,
        'sen': 38
    }
    
    lengths = []
    for i in range(1, n + 1):
        parts = data[i].split()
        num = int(parts[0])
        unit = parts[1]
        length_m = num * conversion[unit]
        lengths.append((length_m, i))
    
    lengths.sort(key=lambda x: x[0])
    arr = [x[0] for x in lengths]
    indices = [x[1] for x in lengths]
    
    max_area = 0.0
    best_triple = None
    
    for i in range(len(arr) - 2):
        a, b, c = arr[i], arr[i+1], arr[i+2]
        if a + b > c:
            p = (a + b + c) / 2.0
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            if area > max_area:
                max_area = area
                best_triple = (indices[i], indices[i+1], indices[i+2])
    
    print("{:.10f}".format(max_area / 4.0))
    print(" ".join(map(str, best_triple)))

if __name__ == "__main__":
    main()
