
def main():
    with open('INPUT.TXT', 'r') as f:
        N, K = map(int, f.readline().split())
    
    numbers = []
    for i in range(1, N + 1):
        numbers.append(str(i))
    
    numbers.sort()
    
    k_str = str(K)
    for i, num in enumerate(numbers):
        if num == k_str:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(str(i + 1))
            return

if __name__ == '__main__':
    main()
