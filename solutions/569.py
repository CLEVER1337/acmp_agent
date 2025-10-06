
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    di = list(map(int, data[2:2+n]))
    
    employees = []
    for i, salary in enumerate(di):
        employees.append((salary, i))
    
    employees.sort()
    
    result = [[0, 0] for _ in range(n)]
    left = 0
    right = n - 1
    
    while left < right:
        low_salary, low_idx = employees[left]
        high_salary, high_idx = employees[right]
        
        needed = d - low_salary
        excess = high_salary - d
        
        if needed <= 0:
            left += 1
            continue
        
        if excess <= 0:
            right -= 1
            continue
        
        transfer_amount = min(needed, excess)
        
        result[low_idx][0] = high_idx + 1
        result[low_idx][1] = transfer_amount
        
        result[high_idx][0] = 0
        result[high_idx][1] = 0
        
        employees[left] = (low_salary + transfer_amount, low_idx)
        employees[right] = (high_salary - transfer_amount, high_idx)
        
        if low_salary + transfer_amount >= d:
            left += 1
        
        if high_salary - transfer_amount <= d:
            right -= 1
    
    for i in range(n):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
