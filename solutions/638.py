
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    k = int(data[1])
    w = int(data[2])
    dw = int(data[3])
    s = int(data[4])
    
    weekly_bad_days = set()
    idx = 5
    for i in range(dw):
        weekly_bad_days.add(int(data[idx]))
        idx += 1
        
    dm = int(data[idx])
    idx += 1
    
    monthly_bad_days = set()
    for i in range(dm):
        monthly_bad_days.add(int(data[idx]))
        idx += 1
        
    total_bad_days = set()
    
    for day in range(1, n + 1):
        day_of_week = (s + day - 2) % w + 1
        if day_of_week in weekly_bad_days or day in monthly_bad_days:
            total_bad_days.add(day)
            
    good_days = [0] * (n + 2)
    for day in range(1, n + 1):
        if day not in total_bad_days:
            good_days[day] = 1
            
    prefix = [0] * (n + 2)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + good_days[i]
        
    count = 0
    for start in range(1, n - k + 2):
        end = start + k - 1
        if prefix[end] - prefix[start - 1] == k:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
