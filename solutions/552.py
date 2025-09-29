
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
        result += counts[i] * (prefix_sum - counts[i]) * (prefix_sum - counts[i] - 1) // 2
    
    result = (result - total) // 3
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
