
with open('INPUT.TXT', 'r') as f:
    A = f.readline().strip()
    B = int(f.readline().strip())

result = int(A) // B
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
