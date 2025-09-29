
import sys

def convert_to_meters(length, unit):
    if unit == 'm':
        return length
    elif unit == 'km':
        return length * 1000
    elif unit == 'mile':
        return length * 1609
    elif unit == 'uin':
        return length * 33
    elif unit == 'kairi':
        return length * 1852
    elif unit == 'zhang':
        return length * 3
    elif unit == 'sen':
        return length * 38

def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    segments = []
    
    for i in range(1, n + 1):
        parts = data[i].split()
        length = float(parts[0])
        unit = parts[1]
        meters = convert_to_meters(length, unit)
        segments.append((meters, i))
    
    segments.sort(key=lambda x: x[0])
    lengths = [seg[0] for seg in segments]
    indices = [seg[1] for seg in segments]
    
    max_area = 0
    best_triangle = []
    
    for i in range(len(lengths) - 2):
        a = lengths[i]
        b = lengths[i + 1]
        c = lengths[i + 2]
        
        if a + b > c:
            area = heron(a, b, c)
            if area > max_area:
                max_area = area
                best_triangle = [indices[i], indices[i + 1], indices[i + 2]]
    
    area_in_talang_wahah = max_area / 4
    print(f"{area_in_talang_wahah:.10f}")
    print(f"{best_triangle[0]} {best_triangle[1]} {best_triangle[2]}")

if __name__ == "__main__":
    main()
