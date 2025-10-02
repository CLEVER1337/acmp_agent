
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        counts = list(map(int, f.readline().split()))
    
    total = 0
    prefix_sum = 0
    
    for i in range(n):
        total += prefix_sum * counts[i]
        prefix_sum += counts[i]
    
    result = 0
    for i in range(n):
        if counts[i] >= 3:
            result += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
    
    for i in range(n):
        if counts[i] >= 2:
            ways = counts[i] * (counts[i] - 1) // 2
            total_others = prefix_sum - counts[i]
            result += ways * total_others
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
