
def main():
    with open('INPUT.TXT', 'r') as f:
        a_str = f.readline().strip()
        b_str = f.readline().strip()
    
    max_len = max(len(a_str), len(b_str)) + 10
    a_arr = [0] * max_len
    b_arr = [0] * max_len
    
    for i, char in enumerate(a_str[::-1]):
        a_arr[i] = int(char)
    
    for i, char in enumerate(b_str[::-1]):
        b_arr[i] = int(char)
    
    res = [a_arr[i] + b_arr[i] for i in range(max_len)]
    
    changed = True
    while changed:
        changed = False
        for i in range(max_len - 2, -1, -1):
            if res[i] >= 1 and res[i+1] >= 1:
                min_val = min(res[i], res[i+1])
                res[i] -= min_val
                res[i+1] -= min_val
                res[i+2] += min_val
                changed = True
                
        for i in range(max_len):
            if res[i] >= 2:
                if i == 0:
                    res[0] -= 2
                    res[1] += 1
                    changed = True
                elif i == 1:
                    res[1] -= 2
                    res[0] += 1
                    res[2] += 1
                    changed = True
                else:
                    res[i] -= 2
                    res[i-2] += 1
                    res[i+1] += 1
                    changed = True
                    
        for i in range(max_len - 1):
            if res[i] >= 1 and res[i+1] >= 1:
                min_val = min(res[i], res[i+1])
                res[i] -= min_val
                res[i+1] -= min_val
                res[i+2] += min_val
                changed = True
    
    output = []
    start_index = max_len - 1
    while start_index >= 0 and res[start_index] == 0:
        start_index -= 1
        
    if start_index < 0:
        output = ['0']
    else:
        for i in range(start_index, -1, -1):
            output.append(str(res[i]))
            
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(output))

if __name__ == '__main__':
    main()
