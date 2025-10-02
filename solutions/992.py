
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    m = list(map(int, data[1:1+k]))
    
    n = sum(m)
    if n == 0:
        print(0)
        return
        
    result = []
    stack = []
    i = 0
    while i < k:
        count = 1
        while i + 1 < k and m[i] == m[i+1]:
            count += 1
            i += 1
        stack.append((m[i], count))
        i += 1
        
    def dfs(pos, current_len, current_count, path):
        if pos == len(stack):
            if current_count > 0:
                path.append((current_len, current_count))
            if path:
                res = []
                for l, cnt in path:
                    res.extend([l] * cnt)
                result.append(res)
            else:
                result.append([])
            return
            
        l, cnt = stack[pos]
        if current_count == 0:
            for take in range(cnt + 1):
                rem = cnt - take
                if rem == 0:
                    dfs(pos + 1, 0, 0, path + [(l, take)])
                else:
                    if take > 0:
                        dfs(pos + 1, l, rem, path + [(l, take - 1)])
                    else:
                        dfs(pos + 1, l, rem, path)
        else:
            if l < current_len:
                return
            min_take = max(0, cnt - (current_len - l if current_len > l else 0))
            for take in range(min_take, cnt + 1):
                rem = cnt - take
                if rem == 0:
                    if l == current_len:
                        dfs(pos + 1, 0, 0, path + [(current_len, current_count + take)])
                    else:
                        dfs(pos + 1, 0, 0, path + [(current_len, current_count), (l, take)])
                else:
                    if l == current_len:
                        dfs(pos + 1, l, current_count + rem, path + [(current_len, take)])
                    else:
                        dfs(pos + 1, l, rem, path + [(current_len, current_count), (l, take)])
                        
    dfs(0, 0, 0, [])
    
    result = sorted(result, key=lambda x: (-len(x), x))
    unique_result = []
    for i, res in enumerate(result):
        if i == 0 or res != result[i-1]:
            unique_result.append(res)
            
    print(len(unique_result))
    for res in unique_result:
        if not res:
            print(0)
        else:
            print(len(res), end=' ')
            print(' '.join(map(str, res)))
            
if __name__ == '__main__':
    main()
