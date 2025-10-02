
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
        
        if low_salary == d and high_salary == d:
            break
            
        if low_salary < d:
            needed = d - low_salary
            available = high_salary - d
            
            transfer = min(needed, available)
            
            if transfer > 0:
                result[high_idx][0] = low_idx + 1
                result[high_idx][1] = transfer
                
                employees[left] = (low_salary + transfer, low_idx)
                employees[right] = (high_salary - transfer, high_idx)
                
                if low_salary + transfer == d:
                    left += 1
                if high_salary - transfer == d:
                    right -= 1
            else:
                right -= 1
        else:
            left += 1
    
    for i in range(n):
        if result[i][0] == 0:
            print("0 0")
        else:
            print(f"{result[i][0]} {result[i][1]}")

if __name__ == "__main__":
    main()
