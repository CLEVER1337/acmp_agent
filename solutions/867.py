
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    coords = list(map(int, data[2:2+n]))
    
    students = sorted([(coords[i], i) for i in range(n)])
    result = [0] * n
    color = 1
    left_ptr = 0
    
    for i in range(n):
        pos, idx = students[i]
        while left_ptr < i and pos - students[left_ptr][0] > d:
            left_ptr += 1
        result[idx] = color
        color = (color % 2) + 1
    
    print(2)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
