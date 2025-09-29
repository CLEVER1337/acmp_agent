
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        a.append(row)
    
    max_vals = [max(row) for row in a]
    company_max = [0] * n
    for i in range(n):
        for j in range(n):
            if a[i][j] == max_vals[i]:
                company_max[i] = j
                break
    
    result = [0] * n
    used = [False] * n
    for i in range(n):
        best_company = -1
        for j in range(n):
            if not used[j]:
                if best_company == -1 or a[j][company_max[i]] > a[best_company][company_max[i]]:
                    best_company = j
        result[best_company] = company_max[i] + 1
        used[best_company] = True
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
