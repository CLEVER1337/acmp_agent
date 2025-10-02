
def main():
    with open("INPUT.TXT", "r") as f:
        N, K = map(int, f.readline().split())
    
    if (K - N) % 2 != 0 or K < N:
        print(0)
        return
    
    steps_to_target = (K - N) // 2
    total_steps = K
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
        return result
    
    result = comb(total_steps, steps_to_target)
    print(result)

if __name__ == "__main__":
    main()
