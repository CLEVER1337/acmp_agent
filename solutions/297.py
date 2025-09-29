
def main():
    with open('INPUT.TXT', 'r') as f:
        n = f.read().strip()
    
    circles = {'0': 1, '6': 1, '8': 2, '9': 1}
    count = 0
    
    for digit in n:
        count += circles.get(digit, 0)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
