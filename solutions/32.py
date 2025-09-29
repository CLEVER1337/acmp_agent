
def max_diff(a, b):
    def get_max(num):
        digits = sorted(str(abs(num)), reverse=True)
        if num < 0:
            digits = sorted(str(abs(num)))
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return -int(''.join(digits))
        else:
            if digits[0] == '0' and len(digits) > 1:
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(digits))
    
    def get_min(num):
        digits = sorted(str(abs(num)))
        if num < 0:
            digits = sorted(str(abs(num)), reverse=True)
            if digits[0] == '0' and len(digits) > 1:
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return -int(''.join(digits))
        else:
            if digits[0] == '0' and len(digits) > 1:
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(digits))
    
    max_a = get_max(a)
    min_b = get_min(b)
    
    return max_a - min_b

def main():
    with open('INPUT.TXT', 'r') as f:
        a, b = map(int, f.read().split())
    
    result = max_diff(a, b)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
