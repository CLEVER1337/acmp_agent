
def main():
    with open('INPUT.TXT', 'r') as f:
        M = int(f.readline().strip())
        N = int(f.readline().strip())
    
    length = N - M + 1
    step = 1
    left = M
    right = N
    
    while length > 1:
        if step % 2 == 1:
            left += (1 << (step - 1))
            length = (length + 1) // 2
        else:
            if length % 2 == 1:
                left += (1 << (step - 1))
            length = length // 2
        step += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(left))

if __name__ == '__main__':
    main()
