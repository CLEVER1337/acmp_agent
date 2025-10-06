
def main():
    n = int(input().strip())
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = n - a - b
            if c <= 0:
                continue
            p1, v1, k1 = a, b, c
            
            v1 += p1
            k1 += p1
            p1 -= (p1 * 2)
            
            p1 += k1
            v1 += k1
            k1 -= (k1 * 2)
            
            p1 += v1
            k1 += v1
            v1 -= (v1 * 2)
            
            if p1 == v1 == k1 and p1 > 0:
                print(a, b, c)
                return
    print("0 0 0")

if __name__ == "__main__":
    main()
