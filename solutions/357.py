
with open('INPUT.TXT', 'r') as f:
    num_str = f.readline().strip()

even_sum = 0
odd_sum = 0

for i, digit in enumerate(num_str):
    if i % 2 == 0:
        odd_sum += int(digit)
    else:
        even_sum += int(digit)

difference = odd_sum - even_sum
if difference % 11 == 0:
    result = "YES"
else:
    result = "NO"

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
