
m, n = map(int, input().split())

if m == 0:
    print('G' * n)
elif n == 0:
    print('B' * m)
else:
    boys = m
    girls = n
    result = []
    
    if boys > girls:
        while boys > 0 and girls > 0:
            result.append('B')
            result.append('G')
            boys -= 1
            girls -= 1
        result.extend(['B'] * boys)
    else:
        while boys > 0 and girls > 0:
            result.append('G')
            result.append('B')
            girls -= 1
            boys -= 1
        result.extend(['G'] * girls)
    
    print(''.join(result))
