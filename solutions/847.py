
with open('INPUT.TXT', 'r') as f:
    word1, word2 = f.readline().split()

if sorted(word1) == sorted(word2):
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES')
else:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')
