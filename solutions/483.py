
n = int(input())
s = input().strip()

if s == '0' * n:
    print('0')
else:
    if s[-1] == '1':
        print(s)
    else:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                break
        if count == 0:
            print(s)
        else:
            result = s[:-count] + '0' * (count - 1) + '1'
            print(result)
