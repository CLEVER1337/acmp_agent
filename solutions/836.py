
n = int(input())
numbers = list(map(int, input().split()))
result = []
for num in numbers:
    if num % 2 == 0:
        octal = oct(num)[2:]
        if len(octal) >= 3:
            third_from_right = octal[-3]
            if int(third_from_right) % 2 == 1:
                result.append(num)
result.sort()
print(len(result))
print(' '.join(map(str, result)))
