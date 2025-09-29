
import math

def main():
    with open("input.txt", "r") as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if N == K:
        print("10 1")
        return
        
    if K == 0:
        if N == 0:
            print("10 1")
        else:
            D = N + 1
            print(f"{D} 1")
        return
        
    best_D = 2
    best_L = 0
    
    divisors = set()
    M = N - K
    
    if M > 0:
        for i in range(1, int(math.isqrt(M)) + 1):
            if M % i == 0:
                divisors.add(i)
                divisors.add(M // i)
        
        for d in divisors:
            if d > max(K, 1) and d <= 10**12:
                temp_N = N
                count = 0
                while temp_N % d == K:
                    count += 1
                    temp_N //= d
                    if temp_N == 0:
                        break
                if count > best_L or (count == best_L and d < best_D):
                    best_L = count
                    best_D = d
    
    if best_L == 0:
        best_D = (N - K) // K + 1
        if best_D <= max(K, 1):
            best_D = N + 1
        best_L = 1
        
    print(f"{best_D} {best_L}")

if __name__ == "__main__":
    main()
