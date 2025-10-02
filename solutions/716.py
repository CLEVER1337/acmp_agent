
def main():
    n = int(input())
    frequencies = []
    comparisons = []
    for i in range(n):
        data = input().split()
        frequencies.append(float(data[0]))
        if i > 0:
            comparisons.append(data[1])
    
    low_bound = 30.0
    high_bound = 4000.0
    
    for i in range(1, n):
        prev_freq = frequencies[i-1]
        curr_freq = frequencies[i]
        comp = comparisons[i-1]
        
        if prev_freq == curr_freq:
            continue
            
        mid = (prev_freq + curr_freq) / 2.0
        
        if comp == 'closer':
            if curr_freq > prev_freq:
                high_bound = min(high_bound, mid)
            else:
                low_bound = max(low_bound, mid)
        else:
            if curr_freq > prev_freq:
                low_bound = max(low_bound, mid)
            else:
                high_bound = min(high_bound, mid)
                
    print(f"{low_bound:.6f} {high_bound:.6f}")

if __name__ == "__main__":
    main()
