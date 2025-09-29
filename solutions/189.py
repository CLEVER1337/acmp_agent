
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        k = int(f.readline().strip())
    
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    
    used = [False] * (n + 1)
    result = []
    
    for i in range(n, 0, -1):
        f = fact[i - 1]
        for num in range(1, n + 1):
            if not used[num]:
                if k > f:
                    k -= f
                else:
                    result.append(str(num))
                    used[num] = True
                    break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
