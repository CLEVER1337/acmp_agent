
def partitions(n):
    def part(n, max_val, prefix):
        if n == 0:
            result.append(prefix)
            return
        for i in range(min(max_val, n), 0, -1):
            part(n - i, i, prefix + [i])
    
    result = []
    part(n, n, [])
    return result

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())

partitions_list = partitions(n)

with open('OUTPUT.TXT', 'w') as f:
    for p in partitions_list:
        f.write('+'.join(map(str, p)) + '\n')
