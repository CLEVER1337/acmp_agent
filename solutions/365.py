
def partitions(n, max_val=None):
    if max_val is None:
        max_val = n
    if n == 0:
        return [[]]
    result = []
    for i in range(min(max_val, n), 0, -1):
        for p in partitions(n - i, i):
            result.append([i] + p)
    return result

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    parts = partitions(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        for part in parts:
            f.write('+'.join(map(str, part)) + '\n')

if __name__ == '__main__':
    main()
