
def main():
    n = int(input().strip())
    if n == 1:
        print("10 0")
        return
        
    from itertools import product
    count = 0
    min_num = None
    
    digits = list(range(1, 10))
    for comb in product(digits, repeat=n):
        if comb[0] == 0:
            continue
        s = sum(comb)
        p = 1
        for d in comb:
            p *= d
            if p > s:
                break
        if p == s:
            count += 1
            num = int(''.join(map(str, comb)))
            if min_num is None or num < min_num:
                min_num = num
                
    if count == 0:
        print("0 0")
    else:
        print(f"{count} {min_num}")

if __name__ == "__main__":
    main()
