
def generate_partitions(n):
    def backtrack(remaining, start, path):
        if remaining == 0:
            partitions.append(path[:])
            return
        for i in range(start, remaining + 1):
            if i <= remaining:
                path.append(i)
                backtrack(remaining - i, i, path)
                path.pop()
    
    partitions = []
    backtrack(n, 1, [])
    return partitions

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    partitions = generate_partitions(n)
    
    with open('OUTPUT.TXT', 'w') as f:
        for partition in partitions:
            f.write('+'.join(map(str, partition)) + '\n')

if __name__ == '__main__':
    main()
