
import re

with open('INPUT.TXT', 'r') as f:
    packed = f.read().strip()

result = []
i = 0
n = len(packed)

while i < n:
    if packed[i].isdigit():
        num_str = ''
        while i < n and packed[i].isdigit():
            num_str += packed[i]
            i += 1
        count = int(num_str)
        char = packed[i]
        result.append(char * count)
        i += 1
    else:
        result.append(packed[i])
        i += 1

original = ''.join(result)

with open('OUTPUT.TXT', 'w') as f:
    for i in range(0, len(original), 40):
        f.write(original[i:i+40] + '\n')
