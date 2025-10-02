
s = input().strip()
count = 0
for i in range(len(s) - 4):
    substr = s[i:i+5]
    if substr == '>>-->' or substr == '<--<<':
        count += 1
print(count)
