
def solve(n):
    sum_ = 0
    for i in range(1, 10**n):
        num = str(i)
        if '0' not in num:
            product = 1
            for digit in num:
                product *= int(digit)
            sum_ += product
    return sum_

with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())

result = solve(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
