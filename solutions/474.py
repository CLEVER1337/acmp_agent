
def keane_bit(n):
    if n == 1:
        return '0'
    
    length = 1
    while length < n:
        length = length * 2 + 1
    
    while length > 1:
        half = (length - 1) // 2
        if n == half + 1:
            return '0'
        elif n > half + 1:
            n = n - half - 1
            length = half
        else:
            length = half
    
    return '0'

n = int(input())
result = keane_bit(n)
print(result)
