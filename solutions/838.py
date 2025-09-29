
def energy_for_char(c):
    if c.islower():
        num = ord(c) - ord('a') + 1
        return sum(int(d) for d in str(num))
    elif c.isupper():
        num = ord(c) - ord('A') + 1
        return sum(int(d) for d in str(num)) + 10
    elif c == ' ':
        return 4
    elif c.isdigit():
        return 13 - int(c)
    elif c == '.':
        return 5
    elif c == ';':
        return 7
    elif c == ',':
        return 2
    elif c in {'=', '+', '-', '"', "'"}:
        return 3
    elif c in {'(', ')'}:
        return 1
    elif c in {'{', '}', '[', ']', '<', '>'}:
        return 8
    return 0

with open('INPUT.TXT', 'r') as f:
    template = f.read()

total_energy = 0
for char in template:
    if char != '\n':
        total_energy += energy_for_char(char)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(total_energy))
