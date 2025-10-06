
def main():
    n = int(input().strip())
    if n == 2:
        print(1)
        return
        
    count = 0
    for k in range(2, n + 1):
        total = n + k
        product = k
        numbers = [1] * (n - 1)
        numbers.append(k)
        
        idx = n - 2
        while idx >= 0:
            while numbers[idx] < numbers[idx + 1] and product * numbers[idx] <= total + (numbers[idx] - 1):
                product = product // numbers[idx] * (numbers[idx] + 1)
                total += 1
                numbers[idx] += 1
                
            if product == total:
                count += 1
                
            if idx == 0:
                break
                
            product = product // numbers[idx] * numbers[idx - 1]
            total = total - numbers[idx] + numbers[idx - 1]
            numbers[idx] = numbers[idx - 1]
            idx -= 1
            
    print(count)

if __name__ == "__main__":
    main()
