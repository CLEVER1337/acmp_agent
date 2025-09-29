
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
    
    if N == 1:
        result = K - 1
    else:
        dp0 = [0] * (N + 1)
        dp1 = [0] * (N + 1)
        dp0[1] = 0
        dp1[1] = K - 1
        
        for i in range(2, N + 1):
            dp0[i] = dp1[i - 1]
            dp1[i] = (dp0[i - 1] + dp1[i - 1]) * (K - 1)
        
        result = dp0[N] + dp1[N]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
