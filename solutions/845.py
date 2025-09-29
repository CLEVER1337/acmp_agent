
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        x = data[0].strip()
        y = data[1].strip()
    
    if y == '0':
        result = 1
    else:
        last_digit_x = int(x[-1])
        exp = int(y[-2:]) if len(y) >= 2 else int(y)
        exp = exp % 4
        if exp == 0:
            exp = 4
        
        result = (last_digit_x ** exp) % 10
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
