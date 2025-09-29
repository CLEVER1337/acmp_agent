
def main():
    with open('INPUT.TXT', 'r') as f:
        a, b, c = map(int, f.read().split())
    
    memo = {}
    
    def F(a, b, c):
        if (a, b, c) in memo:
            return memo[(a, b, c)]
            
        if a <= 0 or b <= 0 or c <= 0:
            result = 1
        elif a > 20 or b > 20 or c > 20:
            result = F(20, 20, 20)
        elif a < b < c:
            result = F(a, b, c-1) + F(a, b-1, c-1) - F(a, b-1, c)
        else:
            result = F(a-1, b, c) + F(a-1, b-1, c) + F(a-1, b, c-1) - F(a-1, b-1, c-1)
        
        memo[(a, b, c)] = result
        return result
    
    result = F(a, b, c)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
