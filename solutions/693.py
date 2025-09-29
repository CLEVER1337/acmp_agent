
with open('INPUT.TXT', 'r') as f:
    s1, s2 = f.readline().strip().split()

s1_lower = s1.lower()
s2_lower = s2.lower()

if sorted(s1_lower) == sorted(s2_lower):
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Yes')
else:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('No')
