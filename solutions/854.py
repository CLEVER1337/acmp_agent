
troom, tcond = map(int, input().split())
mode = input().strip()

if mode == 'freeze':
    result = min(troom, tcond)
elif mode == 'heat':
    result = max(troom, tcond)
elif mode == 'auto':
    result = tcond
elif mode == 'fan':
    result = troom

print(result)
