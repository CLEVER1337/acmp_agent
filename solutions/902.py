
def main():
    n = int(input().strip())
    s = input().strip()
    total_len = len(s)
    
    def solve(pos, left, right, fold_seq):
        if left == right:
            return fold_seq
        mid = (left + right) // 2
        if s[mid] == 'O':
            return None
        
        left_res = solve(2*pos, left, mid, fold_seq + 'P')
        if left_res is not None:
            return left_res
        
        right_res = solve(2*pos+1, mid+1, right, fold_seq + 'Z')
        return right_res

    result = solve(1, 0, total_len-1, "")
    if result is None:
        print("NO")
    else:
        print(result)

if __name__ == '__main__':
    main()
