
def main():
    n = int(input().strip())
    result = []
    def backtrack(s, left, right, square_left, square_right):
        if len(s) == n:
            result.append(s)
            return
        if left < n // 2:
            backtrack(s + '(', left + 1, right, square_left, square_right)
        if right < left:
            backtrack(s + ')', left, right + 1, square_left, square_right)
        if square_left < n // 2:
            backtrack(s + '[', left, right, square_left + 1, square_right)
        if square_right < square_left:
            backtrack(s + ']', left, right, square_left, square_right + 1)
    
    backtrack('', 0, 0, 0, 0)
    with open('OUTPUT.TXT', 'w') as f:
        for expr in result:
            f.write(expr + '\n')

if __name__ == '__main__':
    main()
