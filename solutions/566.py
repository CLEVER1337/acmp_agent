
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        A = int(data[0])
        B = int(data[1])
        C = int(data[2])
        K = int(data[3])
    
    total_stars = A * 1 + B * 2 + C * 3
    max_t_shirts = min(total_stars // K, A + B + C)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_t_shirts))

if __name__ == "__main__":
    main()
