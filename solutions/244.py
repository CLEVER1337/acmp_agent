
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])
    
    error_possible = False
    error_index = -1
    
    for group_idx, group in enumerate(groups):
        count0 = group.count(0)
        count1 = len(group) - count0
        
        if count0 != 0 and count1 != 0:
            if count0 == 1 or count1 == 1:
                if not error_possible:
                    error_possible = True
                    if count0 == 1:
                        error_pos = group.index(0)
                    else:
                        error_pos = group.index(1)
                    error_index = error_pos * k + group_idx + 1
                else:
                    print("FAIL")
                    return
            else:
                print("FAIL")
                return
    
    if error_possible:
        print("OK")
        print(error_index)
    else:
        print("OK")
        print(0)

if __name__ == "__main__":
    main()
