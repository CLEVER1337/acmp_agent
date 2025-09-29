
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def main():
    n = int(input().strip())
    
    if n <= 3:
        print(f"{n} 1")
        return
        
    count_3 = 0
    remainder = n
    
    if remainder % 3 == 1 and remainder > 4:
        count_3 = (remainder - 4) // 3
        remainder = 4
    else:
        count_3 = remainder // 3
        remainder = remainder % 3
        
    if remainder == 1:
        count_3 -= 1
        remainder += 3
        
    result = {}
    if count_3 > 0:
        result[3] = count_3
        
    if remainder == 2:
        result[2] = 1
    elif remainder == 4:
        result[2] = 2
        
    sorted_keys = sorted(result.keys())
    for prime in sorted_keys:
        print(f"{prime} {result[prime]}")
        
if __name__ == "__main__":
    main()
