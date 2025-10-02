
def main():
    import sys
    N = int(sys.stdin.readline().strip())
    
    if N == 2:
        print(1)
        return
        
    count = 0
    for k in range(2, N + 1):
        product = k
        sum_val = k
        numbers = [1] * (N - k) + [k]
        
        if len(numbers) != N:
            continue
            
        for i in range(N - k - 1, -1, -1):
            while numbers[i] < numbers[i + 1]:
                if sum_val + 1 <= product * (numbers[i] + 1) / numbers[i]:
                    sum_val += 1
                    product = product * (numbers[i] + 1) // numbers[i]
                    numbers[i] += 1
                else:
                    break
                    
        if sum_val == product:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
