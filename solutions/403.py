
def count_up_to(n):
    s = str(n)
    length = len(s)
    count = 0
    digits = [0] * 10
    used = [False] * length
    
    def dfs(pos, tight, leading_zero):
        nonlocal count
        if pos == length:
            if not leading_zero:
                count += 1
            return
        
        limit = int(s[pos]) if tight else 9
        for d in range(0, limit + 1):
            if digits[d] >= 2:
                continue
            if leading_zero and d == 0:
                digits[d] += 1
                dfs(pos + 1, tight and (d == limit), True)
                digits[d] -= 1
            else:
                if digits[d] < 2:
                    digits[d] += 1
                    dfs(pos + 1, tight and (d == limit), False)
                    digits[d] -= 1
    
    dfs(0, True, True)
    return count

def main():
    L, R = map(int, input().split())
    result_R = count_up_to(R)
    result_L_minus = count_up_to(L - 1)
    print(result_R - result_L_minus)

if __name__ == "__main__":
    main()
