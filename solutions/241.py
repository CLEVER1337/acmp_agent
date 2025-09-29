
def main():
    K = int(input().strip())
    
    max_consecutive = 0
    for start_day in range(7):
        calendar = [0] * 366
        
        for i in range(366):
            weekday = (start_day + i) % 7
            if weekday == 5 or weekday == 6:
                calendar[i] = 1
        
        for i in range(K):
            calendar[i] = 1
        
        feb_23 = 31 + 22
        mar_8 = 31 + 28 + 7
        
        calendar[feb_23] = 1
        calendar[mar_8] = 1
        
        for i in range(366):
            if calendar[i] == 0:
                continue
            j = i
            while j < 366 and calendar[j] == 1:
                j += 1
            max_consecutive = max(max_consecutive, j - i)
    
    print(max_consecutive)

if __name__ == "__main__":
    main()
