
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    performances = []
    index = 3
    for i in range(p):
        athlete = int(data[index])
        exercise = int(data[index + 1])
        index += 2
        performances.append((athlete, exercise))
    
    count = 0
    for i in range(p):
        a1, e1 = performances[i]
        for j in range(i):
            a2, e2 = performances[j]
            if a1 > a2 and e1 < e2:
                count += 1
            elif a1 < a2 and e1 > e2:
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()
