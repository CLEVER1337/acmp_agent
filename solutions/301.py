
def main():
    with open("INPUT.TXT", "r") as f:
        S, K = map(int, f.readline().split())
    
    # Максимальное число
    max_num = []
    remaining = S
    for i in range(K):
        digit = min(9, remaining)
        max_num.append(str(digit))
        remaining -= digit
    
    # Минимальное число
    min_num = []
    remaining = S
    for i in range(K):
        pos_left = K - i - 1
        if i == 0:
            digit = max(1, remaining - 9 * pos_left)
        else:
            digit = max(0, remaining - 9 * pos_left)
        min_num.append(str(digit))
        remaining -= digit
    
    max_str = ''.join(max_num)
    min_str = ''.join(min_num)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{max_str} {min_str}")

if __name__ == "__main__":
    main()
