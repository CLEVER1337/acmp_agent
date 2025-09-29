
def generate(n):
    result = []
    def backtrack(s, left1, right1, left2, right2):
        if len(s) == n:
            result.append(s)
            return
        if left1 < n // 2:
            backtrack(s + '(', left1 + 1, right1, left2, right2)
        if left2 < n // 2:
            backtrack(s + '[', left1, right1, left2 + 1, right2)
        if right1 < left1:
            backtrack(s + ')', left1, right1 + 1, left2, right2)
        if right2 < left2:
            backtrack(s + ']', left1, right1, left2, right2 + 1)
    
    backtrack('', 0, 0, 0, 0)
    return result

n = int(open('INPUT.TXT').read().strip())
expressions = generate(n)
with open('OUTPUT.TXT', 'w') as f:
    for expr in expressions:
        f.write(expr + '\n')
