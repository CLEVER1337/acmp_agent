
def main():
    with open('INPUT.TXT', 'r') as f:
        a, b = map(int, f.readline().split())
    
    automorphic_numbers = []
    
    for num in range(a, b + 1):
        square = num * num
        num_str = str(num)
        square_str = str(square)
        
        if square_str.endswith(num_str):
            automorphic_numbers.append(num)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, automorphic_numbers)))

if __name__ == "__main__":
    main()
