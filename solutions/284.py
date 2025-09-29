
with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))
    m = int(f.readline().strip())
    pairs = [tuple(map(int, line.split())) for line in f.readlines()]

with open('OUTPUT.TXT', 'w') as f:
    for i, j in pairs:
        subarray = arr[i-1:j]
        f.write(' '.join(map(str, subarray)) + '\n')
