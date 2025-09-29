
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
    
    total = 2 ** n
    count = 0
    
    for i in range(m):
        count += comb(n, i)
    
    result = total - count
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res

if __name__ == "__main__":
    main()
