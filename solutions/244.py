
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])
    
    error_count = 0
    error_pos = -1
    
    for group_idx, group in enumerate(groups):
        count0 = group.count(0)
        count1 = len(group) - count0
        
        if count0 != count1:
            if abs(count0 - count1) > 1:
                error_count += 1
                if error_count > 1:
                    print("FAIL")
                    return
                
                majority = 0 if count0 > count1 else 1
                for pos_in_group, val in enumerate(group):
                    if val != majority:
                        candidate_error = group_idx + pos_in_group * k + 1
                        if error_pos == -1 or candidate_error < error_pos:
                            error_pos = candidate_error
    
    if error_count == 0:
        print("OK")
        print(0)
    else:
        print("OK")
        print(error_pos)

if __name__ == "__main__":
    main()
