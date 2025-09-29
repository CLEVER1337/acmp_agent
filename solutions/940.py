
with open('INPUT.TXT', 'r') as f:
    data = f.read().split()
    k = int(data[0])
    word = ''.join(data[1:])
    result = word[:k-1] + word[k:]
    with open('OUTPUT.TXT', 'w') as out:
        out.write(result)
