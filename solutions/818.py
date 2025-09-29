
n = int(input())
a = list(map(int, input().split()))
total_sockets = 1
for ai in sorted(a, reverse=True):
    if total_sockets <= 0:
        break
    total_sockets += ai - 1
print(total_sockets)
