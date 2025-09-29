
with open('INPUT.TXT', 'r') as f:
    card = list(map(int, f.readline().split()))
    envelope = list(map(int, f.readline().split()))

card.sort()
envelope.sort()

if card[0] <= envelope[0] and card[1] <= envelope[1]:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Possible')
else:
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Impossible')
