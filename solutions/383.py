
def is_beautiful(num):
    s = str(num)
    total = sum(int(d) for d in s)
    return total % len(s) == 0

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    count = 0
    num = 1
    while count < N:
        if is_beautiful(num):
            count += 1
        num += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(num - 1))

if __name__ == '__main__':
    main()
