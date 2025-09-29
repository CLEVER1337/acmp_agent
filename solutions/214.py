
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
    
    total_heads = 2 * n + 3 * m
    
    if total_heads == 0:
        print(2)
        return
        
    grundy = 0
    
    for _ in range(n):
        grundy ^= 1
        
    for _ in range(m):
        grundy ^= 2
        
    if grundy != 0:
        result = 1
    else:
        result = 2
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
