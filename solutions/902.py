
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    s = data[1].strip()
    
    if n == 0:
        print("")
        return
        
    length = len(s)
    if length != (1 << n) - 1:
        print("NO")
        return
        
    def dfs(l, r, fold_type):
        if l == r:
            return ""
        mid = (l + r) // 2
        left_str = dfs(l, mid, 'P')
        right_str = dfs(mid + 1, r, 'Z')
        
        if left_str is None or right_str is None:
            return None
            
        if fold_type == 'P':
            if s[mid] == 'K':
                return left_str + 'P' + right_str
            else:
                return None
        else:
            if s[mid] == 'O':
                return left_str + 'Z' + right_str
            else:
                return None
                
    result = dfs(0, length - 1, 'P')
    if result is not None:
        print(result)
        return
        
    result = dfs(0, length - 1, 'Z')
    if result is not None:
        print(result)
        return
        
    print("NO")

if __name__ == "__main__":
    main()
