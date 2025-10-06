
def main():
    n = input().strip()
    total = 0
    len_n = len(n)
    for digits in range(1, len_n + 1):
        start = 10 ** (digits - 1)
        end = 10 ** digits - 1
        if digits < len_n:
            count = end - start + 1
            total += count * digits
        else:
            num = int(n)
            count = num - start + 1
            total += count * digits
            break
            
    target = int(n)
    pos = total - (len_n * (target - int(n) + 1)) + 1
    
    for digits in range(1, len_n):
        start = 10 ** (digits - 1)
        end = 10 ** digits - 1
        for num in range(start, end + 1):
            s = str(num)
            if len(s) + len_n - 1 <= digits:
                continue
            for i in range(len(s) - len_n + 1):
                if i + len_n <= len(s):
                    if s[i:i+len_n] == n:
                        offset = total - (len_n * (target - int(n) + 1)) - (len(s) * (end - num + 1))
                        for check in range(start, num):
                            offset += len(str(check))
                        return print(offset + i + 1)
                else:
                    remaining = len_n - (len(s) - i)
                    next_num = num + 1
                    if next_num <= end:
                        next_s = str(next_num)
                        if len(next_s) >= remaining:
                            combined = s[i:] + next_s[:remaining]
                            if combined == n:
                                offset = total - (len_n * (target - int(n) + 1)) - (len(s) * (end - num + 1))
                                for check in range(start, num):
                                    offset += len(str(check))
                                return print(offset + i + 1)
    
    print(pos)

if __name__ == '__main__':
    main()
