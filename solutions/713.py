
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    func_desc = list(map(int, data[1].split()))
    f00, f01, f10, f11 = func_desc
    
    if n == 2:
        if f00 == 1:
            print("00")
        elif f01 == 1:
            print("01")
        elif f10 == 1:
            print("10")
        elif f11 == 1:
            print("11")
        else:
            print("No solution")
        return

    if f00 == 0 and f01 == 0 and f10 == 0 and f11 == 0:
        print("No solution")
        return
        
    if f11 == 1:
        result = ['1'] * n
        print(''.join(result))
        return
        
    if f00 == 1:
        result = ['0'] * n
        print(''.join(result))
        return
        
    if f01 == 1 and f10 == 1:
        if n % 2 == 1:
            result = ['1'] * n
            print(''.join(result))
        else:
            result = ['1'] * (n-1) + ['0']
            print(''.join(result))
        return
        
    if f01 == 1:
        if f00 == 1:
            result = ['0'] * n
            print(''.join(result))
            return
        if n % 2 == 0:
            result = ['1'] * n
            print(''.join(result))
        else:
            result = ['1'] * (n-1) + ['0']
            print(''.join(result))
        return
        
    if f10 == 1:
        if f00 == 1:
            result = ['0'] * n
            print(''.join(result))
            return
        if n % 2 == 0:
            result = ['1'] * n
            print(''.join(result))
        else:
            result = ['0'] + ['1'] * (n-1)
            print(''.join(result))
        return

    print("No solution")

if __name__ == "__main__":
    main()
