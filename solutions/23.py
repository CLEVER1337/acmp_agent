
def divine_sum(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    return total

with open('INPUT.TXT', 'r') as file:
    n = int(file.read())

result = divine_sum(n)

with open('OUTPUT.TXT', 'w') as file:
    file.write(str(result))
