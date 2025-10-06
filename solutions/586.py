
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Crisis")
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    prefs = []
    index = 3
    for i in range(n):
        row = list(map(int, data[index:index+k]))
        index += k
        prefs.append(row)
    
    if k == 0:
        print("Crisis")
        return
        
    votes_needed = m
    current_law = k
    
    for law in range(k-1, -1, -1):
        count = 0
        for i in range(n):
            for pref in prefs[i]:
                if pref == law + 1:
                    count += 1
                    break
                elif pref == current_law:
                    break
        if count >= votes_needed:
            current_law = law + 1
            
    if current_law == 0:
        print("Crisis")
    else:
        print(current_law)

if __name__ == "__main__":
    main()
