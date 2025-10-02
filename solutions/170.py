
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    max_count = 1
    
    for k in range(2, int((2 * N) ** 0.5) + 2):
        if (2 * N) % k == 0:
            numerator = 2 * N // k - k + 1
            if numerator > 0 and numerator % 2 == 0:
                max_count = max(max_count, k)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_count))

if __name__ == '__main__':
    main()
