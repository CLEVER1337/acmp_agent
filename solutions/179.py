
k = int(input().strip())

if k == 0:
    print(1)
elif k == 1:
    print(2)
else:
    a, b = 1, 1
    total = 2
    for _ in range(k - 1):
        new_numbers = []
        current_sum = a + b
        new_numbers.append(current_sum)
        a, b = b, current_sum
        total += current_sum
        total += current_sum
    
    print(total)
