
def is_beautiful(num):
    s = str(num)
    total = sum(int(d) for d in s)
    return total % len(s) == 0

def find_nth_beautiful(n):
    count = 0
    num = 1
    while count < n:
        if is_beautiful(num):
            count += 1
        num += 1
    return num - 1

n = int(input())
result = find_nth_beautiful(n)
print(result)
