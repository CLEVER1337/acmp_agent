
n = int(input().strip())
if n <= 2:
    print("YES")
    for i in range(n):
        print(f"{i} {i}")
elif n == 3:
    print("YES")
    print("0 0")
    print("1 0")
    print("0 1")
else:
    print("YES")
    for i in range(n):
        print(f"{i} {i*i}")
