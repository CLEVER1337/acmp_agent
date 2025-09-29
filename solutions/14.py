
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

with open('INPUT.TXT', 'r') as file:
    a, b = map(int, file.readline().split())

result = lcm(a, b)

with open('OUTPUT.TXT', 'w') as file:
    file.write(str(result))
