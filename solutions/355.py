
from itertools import permutations

with open('INPUT.TXT', 'r') as f:
    s = f.readline().strip()

perms = set(permutations(s))
result = [''.join(p) for p in perms]

with open('OUTPUT.TXT', 'w') as f:
    for perm in result:
        f.write(perm + '\n')
