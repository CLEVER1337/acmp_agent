
import math

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if N == K:
        print("2 1")
        return
        
    if N < K:
        print("2 0")
        return
        
    if K == 0:
        divisors = set()
        n = N
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            i += 1
        divisors = sorted(divisors)
        for d in divisors:
            if d > max(N, 1):
                D = d
                break
        else:
            D = N + 1
        if D > 10**12:
            D = N + 1
        print(f"{D} 1")
        return
        
    best_D = 2
    best_L = 0
    
    def check_base(D):
        if D <= max(K, 1):
            return 0
        temp = N
        count = 0
        while temp > 0:
            remainder = temp % D
            if remainder != K:
                break
            count += 1
            temp //= D
        return count
    
    def find_solution_for_L(L):
        if L == 0:
            return 2, 0
        left = max(K + 1, (N - K) // (N // (10**12)) + 1 if N > 10**12 else 2)
        right = N - K
        if L == 1:
            D_candidate = right
            if D_candidate > max(K, 1) and check_base(D_candidate) >= 1:
                return D_candidate, 1
            return 2, 0
        
        low = max(math.ceil((N - K) / (N // (10**12)) + 1) if N > 10**12 else 2, K + 1)
        high = (N - K) // (K * (L - 1)) if L > 1 else N - K
        
        for D in range(int(low), int(high) + 1):
            if D > 10**12:
                break
            temp = N
            valid = True
            for i in range(L):
                remainder = temp % D
                if remainder != K:
                    valid = False
                    break
                temp //= D
            if valid and temp >= 0:
                return D, L
        return None, None
    
    max_possible_L = 0
    temp_N = N
    while temp_N >= K:
        max_possible_L += 1
        temp_N //= max(K + 1, 2)
    
    found_D = None
    found_L = 0
    
    for L in range(max_possible_L, 0, -1):
        candidate_D, candidate_L = find_solution_for_L(L)
        if candidate_D is not None:
            found_D = candidate_D
            found_L = candidate_L
            break
    
    if found_D is not None:
        print(f"{found_D} {found_L}")
    else:
        D_candidate = (N - K) // K
        if D_candidate > max(K, 1) and check_base(D_candidate) > 0:
            print(f"{D_candidate} {check_base(D_candidate)}")
        else:
            print("2 0")

if __name__ == "__main__":
    main()
