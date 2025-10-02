
import math

def is_powerful(num):
    if num == 1:
        return False
    for exponent in range(2, int(math.log2(num)) + 2):
        root = round(num ** (1.0 / exponent))
        if root < 2:
            continue
        if root ** exponent == num:
            return True
    return False

with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

results = []
for num in numbers:
    if is_powerful(num):
        results.append("YES")
    else:
        results.append("NO")

with open('OUTPUT.TXT', 'w') as f:
    for result in results:
        f.write(result + '\n')
