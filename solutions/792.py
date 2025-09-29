
def sum_digits(n, base):
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total

def main():
    with open('INPUT.TXT', 'r') as f:
        data1 = f.readline().split()
        data2 = f.readline().split()
    
    n1 = int(data1[0])
    p1 = int(data1[1])
    n2 = int(data2[0])
    p2 = int(data2[1])
    
    k1 = sum_digits(n1, p1)
    k2 = sum_digits(n2, p2)
    
    result = k1 if k1 == k2 else 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
