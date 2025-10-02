
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return f(n // 2)
    else:
        k = n // 2
        return f(k) + f(k + 1)

def main():
    with open('INPUT.TXT', 'r') as f_in:
        n = int(f_in.read().strip())
    
    result = f(n)
    
    with open('OUTPUT.TXT', 'w') as f_out:
        f_out.write(str(result))

if __name__ == '__main__':
    main()
