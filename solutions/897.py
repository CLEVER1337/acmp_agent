
import math

def is_powerful(num):
    if num == 1:
        return False
    for base in range(2, int(math.isqrt(num)) + 1):
        power = base
        while power < num:
            power *= base
        if power == num:
            return True
    return False

n = int(input())
numbers = list(map(int, input().split()))
results = []
for num in numbers:
    if is_powerful(num):
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
