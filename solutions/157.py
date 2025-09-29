
from math import factorial
from collections import Counter

word = input().strip()
counts = Counter(word)
total = factorial(len(word))
for count in counts.values():
    total //= factorial(count)
print(total)
