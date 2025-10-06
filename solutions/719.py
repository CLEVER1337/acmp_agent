
import math

def main():
    F_str = input().strip()
    if F_str == '0':
        print(0)
        return
        
    F = int(F_str)
    if F == 1:
        print(1)
        return
        
    low, high = 1, 2 * 10**6
    while low < high:
        mid = (low + high) // 2
        factorial_mid = math.factorial(mid)
        if factorial_mid < F:
            low = mid + 1
        else:
            high = mid
            
    print(low)

if __name__ == "__main__":
    main()
