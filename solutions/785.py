
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

def main():
    with open('INPUT.TXT', 'r') as f:
        a, b = map(int, f.readline().split())
    
    automorphic_numbers = []
    for num in range(a, b + 1):
        if is_automorphic(num):
            automorphic_numbers.append(num)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, automorphic_numbers)))

if __name__ == '__main__':
    main()
