
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
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
        if left_str is None:
            return None
            
        right_str = dfs(mid + 1, r, 'Z')
        if right_str is None:
            return None
            
        if fold_type == 'P':
            if s[mid] != 'O':
                return None
        else:
            if s[mid] != 'K':
                return None
                
        return left_str + fold_type + right_str
        
    result = dfs(0, length - 1, 'P')
    if result is None:
        result = dfs(0, length - 1, 'Z')
        
    if result is None:
        print("NO")
    else:
        print(result)

if __name__ == "__main__":
    main()
