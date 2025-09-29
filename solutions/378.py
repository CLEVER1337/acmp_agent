
n = int(input())
arr = list(map(int, input().split()))

possible_sums = {0}

for num in arr:
    new_sums = set()
    for s in possible_sums:
        new_sums.add(s + num)
    possible_sums |= new_sums

print(len(possible_sums))
