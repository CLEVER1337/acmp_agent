
def solve():
    from itertools import permutations, product
    
    def evaluate(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
    
    def can_make_24(nums):
        ops = ['+', '-', '*']
        
        for perm in permutations(nums):
            a, b, c, d = perm
            
            for op1, op2, op3 in product(ops, repeat=3):
                try:
                    # ((a op1 b) op2 c) op3 d
                    res1 = evaluate(evaluate(evaluate(a, b, op1), c, op2), d, op3)
                    if res1 == 24:
                        return True
                    
                    # (a op1 b) op2 (c op3 d)
                    res2 = evaluate(evaluate(a, b, op1), evaluate(c, d, op3), op2)
                    if res2 == 24:
                        return True
                    
                    # (a op1 (b op2 c)) op3 d
                    res3 = evaluate(evaluate(a, evaluate(b, c, op2), op1), d, op3)
                    if res3 == 24:
                        return True
                    
                    # a op1 ((b op2 c) op3 d)
                    res4 = evaluate(a, evaluate(evaluate(b, c, op2), d, op3), op1)
                    if res4 == 24:
                        return True
                    
                    # a op1 (b op2 (c op3 d))
                    res5 = evaluate(a, evaluate(b, evaluate(c, d, op3), op2), op1)
                    if res5 == 24:
                        return True
                        
                except:
                    continue
        
        return False
    
    nums = list(map(int, input().split()))
    if can_make_24(nums):
        print("YES")
    else:
        print("NO")

solve()
