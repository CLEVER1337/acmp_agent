
n = int(input().strip())
if n <= 2:
    print("YES")
    for i in range(n):
        print(f"{i} {i}")
elif n == 3:
    print("NO")
else:
    print("YES")
    for i in range(n):
        print(f"{i} {i*i}")
