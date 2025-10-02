
with open('INPUT.TXT', 'r') as f:
    words = f.readline().split()
    word1, word2 = words[0], words[1]

if sorted(word1) == sorted(word2):
    result = 'YES'
else:
    result = 'NO'

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
