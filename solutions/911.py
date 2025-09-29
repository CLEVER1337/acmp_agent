
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        C = data[0]
        N = int(data[1])
    
    weights = []
    while N > 0:
        remainder = N % 3
        weights.append(remainder)
        N = N // 3
        if remainder == 2:
            N += 1
    
    left_weights = []
    right_weights = []
    power = 0
    
    for digit in weights:
        if digit == 1:
            if C == 'L':
                right_weights.append(3**power)
            else:
                left_weights.append(3**power)
        elif digit == 2:
            if C == 'L':
                left_weights.append(3**power)
            else:
                right_weights.append(3**power)
        power += 1
    
    left_weights.sort()
    right_weights.sort()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("L: " + " ".join(map(str, left_weights)) + "\n")
        f.write("R: " + " ".join(map(str, right_weights)) + "\n")

if __name__ == "__main__":
    main()
