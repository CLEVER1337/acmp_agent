
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        intervals = []
        for _ in range(n):
            a, b = map(int, f.readline().split())
            intervals.append((a, b))
    
    max_start = max(a for a, b in intervals)
    min_end = min(b for a, b in intervals)
    
    result = 'YES' if max_start <= min_end else 'NO'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
