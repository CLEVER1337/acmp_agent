
s = input().strip()
n = len(s)

if all(c == s[0] for c in s):
    print("NO SOLUTION")
    exit()

left = 0
right = n - 1
while left < right and s[left] == s[right]:
    left += 1
    right -= 1

if left >= right:
    print("NO SOLUTION")
else:
    if all(c == s[0] for c in s[:n-1]):
        print(s[:n-1])
    else:
        print(s)
