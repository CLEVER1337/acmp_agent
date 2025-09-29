
def kaprekar_steps(n):
    steps = 0
    while True:
        s = str(n).zfill(4)
        if len(s) > 4:
            s = s[-4:]
        desc = int(''.join(sorted(s, reverse=True)))
        asc = int(''.join(sorted(s)))
        n = desc - asc
        steps += 1
        if n == 6174:
            return 6174, steps

with open('INPUT.TXT', 'r') as f:
    num = int(f.read().strip())

result, steps_count = kaprekar_steps(num)

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{result}\n{steps_count}")
