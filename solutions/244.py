
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(arr[i])
    
    conflicts = []
    for i in range(k):
        group = groups[i]
        zeros = group.count(0)
        ones = len(group) - zeros
        if zeros == ones:
            conflicts.append(i)
        elif zeros != 0 and ones != 0:
            print("FAIL")
            return
    
    if not conflicts:
        print("OK")
        print(0)
        return
    
    if len(conflicts) > 1:
        print("FAIL")
        return
        
    conflict_group = conflicts[0]
    group = groups[conflict_group]
    zeros = group.count(0)
    ones = len(group) - zeros
    if abs(zeros - ones) != 1:
        print("FAIL")
        return
        
    target = 0 if zeros > ones else 1
    for pos in range(len(group)):
        if group[pos] != target:
            error_index = conflict_group + pos * k + 1
            print("OK")
            print(error_index)
            return
    
    print("FAIL")

if __name__ == "__main__":
    main()
