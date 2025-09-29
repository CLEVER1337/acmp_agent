
with open('INPUT.TXT', 'r') as f:
    coord = f.readline().strip()
    
letter = coord[0]
number = int(coord[1])

letter_num = ord(letter) - ord('A') + 1

if (letter_num + number) % 2 == 0:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('BLACK')
else:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('WHITE')
