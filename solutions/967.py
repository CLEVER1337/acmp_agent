
def sum_digits(n, base):
    total = 0
    while n:
        total += n % base
        n //= base
    return total

def main():
    with open('INPUT.TXT', 'r') as f:
        n, k1, k2 = map(int, f.readline().split())
        a_list = list(map(int, f.readline().split()))
    
    b_list = []
    for ai in a_list:
        s1 = sum_digits(ai, k1)
        s2 = sum_digits(ai, k2)
        b_list.append(s1 * s2)
    
    b_list.sort()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, b_list)))

if __name__ == '__main__':
    main()
