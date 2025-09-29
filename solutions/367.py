
with open('INPUT.TXT', 'r') as f:
    data = f.readline().split()
    A = int(data[0])
    N = int(data[1])

result = str(pow(A, N))

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
