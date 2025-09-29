
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    func = list(map(int, data[1].split()))
    
    f00, f01, f10, f11 = func
    
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
        
    if f01 == f10:
        if f01 == 0:
            if f00 == 1:
                res = ['0'] * n
                print(''.join(res))
            elif f11 == 1:
                res = ['1'] * n
                print(''.join(res))
            else:
                print("No solution")
        else:
            if f00 == 1:
                res = ['0'] * n
                print(''.join(res))
            elif f11 == 1:
                res = ['1'] * n
                print(''.join(res))
            else:
                res = ['0'] * (n - 1) + ['1']
                print(''.join(res))
    else:
        if f01 == 1 and f10 == 0:
            if f00 == 1:
                res = ['0'] * n
                print(''.join(res))
            else:
                if f11 == 1:
                    if n % 2 == 1:
                        res = ['1'] * n
                        print(''.join(res))
                    else:
                        res = ['1'] * (n - 1) + ['0']
                        print(''.join(res))
                else:
                    print("No solution")
        else:
            if f11 == 1:
                res = ['1'] * n
                print(''.join(res))
            else:
                if f00 == 1:
                    if n % 2 == 1:
                        res = ['0'] * n
                        print(''.join(res))
                    else:
                        res = ['0'] * (n - 1) + ['1']
                        print(''.join(res))
                else:
                    print("No solution")

if __name__ == "__main__":
    main()
