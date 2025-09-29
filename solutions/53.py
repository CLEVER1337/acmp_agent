
n, m = map(int, input().split())

red = 0
green = 0
blue = 0
black = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        num = i * j
        if num % 5 == 0:
            blue += 1
        elif num % 3 == 0:
            green += 1
        elif num % 2 == 0:
            red += 1
        else:
            black += 1

print(red)
print(green)
print(blue)
print(black)
