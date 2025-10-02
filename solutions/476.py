
def main():
    with open('INPUT.TXT', 'r') as f:
        m, n = map(int, f.read().split())
    
    if m == n:
        if (m - 1) % 2 == 0:
            print(2)
        else:
            print(1)
    else:
        min_val = min(m, n)
        if min_val % 2 == 1:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()
