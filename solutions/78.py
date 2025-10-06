
def main():
    F, P = map(int, input().split())
    low, high = 1, 2 * 10**9
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        total = mid
        bottles = 0
        for day in range(5):
            if day == 4:
                if total < F:
                    bottles = 0
                else:
                    bottles = total // F
                    total = total % F + bottles * P
            else:
                bottles = total // F
                total = total % F + bottles * P
        
        if bottles == 1 and total == 0:
            result = mid
            high = mid - 1
        elif bottles < 1:
            low = mid + 1
        else:
            high = mid - 1
            
    print(result)

if __name__ == "__main__":
    main()
