
def main():
    n = int(input().strip())
    if n <= 5:
        a_values = [0, 2, 3, 4, 7, 13]
        b_values = [0, 1, 5, 6, 8, 9]
        print(a_values[n])
        print(b_values[n])
        return
        
    max_size = max(10000, n * 2)
    a = [0] * (max_size + 1)
    b = [0] * (max_size + 1)
    used = [False] * (max_size * 2)
    
    a[1], a[2], a[3], a[4], a[5] = 2, 3, 4, 7, 13
    for num in a[1:6]:
        if num <= max_size * 2:
            used[num] = True
            
    b_index = 1
    for i in range(1, max_size * 2):
        if not used[i] and b_index <= max_size:
            b[b_index] = i
            used[i] = True
            b_index += 1
            
    for i in range(6, max_size + 1):
        a[i] = b[i-1] + b[i-3]
        if a[i] < len(used):
            used[a[i]] = True
            
        next_b = b[i-1] + 1
        while used[next_b]:
            next_b += 1
        b[i] = next_b
        used[next_b] = True
        
    print(a[n])
    print(b[n])

if __name__ == "__main__":
    main()
