
def kaprekar_steps(n):
    steps = 0
    while n != 6174:
        digits = str(n).zfill(4)
        asc = int(''.join(sorted(digits)))
        desc = int(''.join(sorted(digits, reverse=True)))
        n = desc - asc
        steps += 1
    return 6174, steps

with open('INPUT.TXT', 'r') as f:
    number = int(f.read().strip())

result, steps_count = kaprekar_steps(number)

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{result}\n{steps_count}")
