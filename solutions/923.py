
def count_groups(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    if n % 2 == 0:
        return count_groups(n // 2) + count_groups(n // 2)
    else:
        return count_groups(n // 2 + 1) + count_groups(n // 2)

n = int(input())
print(count_groups(n))
