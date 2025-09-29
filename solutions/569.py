
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    di = list(map(int, data[2:2+n]))
    
    employees = []
    for i in range(n):
        employees.append((di[i], i))
    
    employees.sort()
    
    result = [[0, 0] for _ in range(n)]
    
    left = 0
    right = n - 1
    
    while left < right:
        if employees[left][0] == d and employees[right][0] == d:
            break
            
        if employees[left][0] < d:
            needed = d - employees[left][0]
            available = employees[right][0] - d
            
            transfer = min(needed, available)
            
            if transfer > 0:
                from_idx = employees[right][1]
                to_idx = employees[left][1]
                
                result[from_idx] = [to_idx + 1, transfer]
                result[to_idx] = [0, 0]
                
                employees[left] = (employees[left][0] + transfer, employees[left][1])
                employees[right] = (employees[right][0] - transfer, employees[right][1])
                
                if employees[left][0] == d:
                    left += 1
                if employees[right][0] == d:
                    right -= 1
            else:
                right -= 1
        else:
            left += 1
    
    for i in range(n):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
