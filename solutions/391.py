
def main():
    with open("INPUT.TXT", "r") as f:
        x, m, L, v = map(int, f.read().split())
    
    max_len = L
    target = v
    
    if m == 1:
        if target == 0:
            print("0" * max_len)
        else:
            print("NO SOLUTION")
        return
    
    for first_digit in range(10):
        S = [first_digit]
        current_hash = first_digit % m
        
        power = 1
        for i in range(1, max_len):
            power = (power * x) % m
            needed = (target - current_hash) % m
            
            for digit in range(10):
                if (digit * power) % m == needed:
                    S.append(digit)
                    current_hash = (current_hash + digit * power) % m
                    break
            else:
                break
        else:
            if current_hash == target:
                print(''.join(map(str, S)))
                return
    
    print("NO SOLUTION")

if __name__ == "__main__":
    main()
