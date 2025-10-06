
def main():
    p, q = map(int, input().split())
    n = 1
    a = []
    i = 2
    while p > 0:
        n += 1
        a_i = (p * i) // q
        a.append(a_i)
        p = p * i - a_i * q
        if p == 0:
            break
        i += 1
        
    print(n)
    for num in a:
        print(num)

if __name__ == "__main__":
    main()
