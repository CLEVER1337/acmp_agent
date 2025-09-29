
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    
    preperiod = 0
    original_n = n
    n = original_n
    
    temp = n
    count2 = 0
    count5 = 0
    
    while temp % 2 == 0:
        count2 += 1
        temp //= 2
    
    while temp % 5 == 0:
        count5 += 1
        temp //= 5
    
    preperiod = max(count2, count5)
    
    if n == 1:
        period = 0
    else:
        k = 1
        while (10**k - 1) % n != 0:
            k += 1
        period = k
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{preperiod} {period}")

if __name__ == "__main__":
    main()
