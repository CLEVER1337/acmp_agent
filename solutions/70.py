
s = input().strip()
k = int(input().strip())

if k > 0:
    result = s * k
    if len(result) > 1023:
        result = result[:1023]
    print(result)
else:
    n = -k
    if len(s) % n != 0:
        print("NO SOLUTION")
    else:
        part_length = len(s) // n
        base = s[:part_length]
        constructed = base * n
        if constructed == s:
            if len(base) > 1023:
                base = base[:1023]
            print(base)
        else:
            print("NO SOLUTION")
