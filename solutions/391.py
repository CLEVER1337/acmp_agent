
def main():
    with open('INPUT.TXT', 'r') as f:
        x, m, L, v = map(int, f.read().split())
    
    if m == 1:
        if v == 0:
            result = '0' * L
        else:
            result = 'NO SOLUTION'
    else:
        S = ['0'] * L
        current_hash = 0
        power = 1
        
        for i in range(L-1, -1, -1):
            for digit in range(9, -1, -1):
                temp_hash = (current_hash + digit * power) % m
                remaining_max = (power - 1) % m if i > 0 else 0
                
                if i > 0:
                    max_possible = (temp_hash + 9 * (power - 1) // (x - 1)) % m
                    min_possible = temp_hash
                else:
                    max_possible = min_possible = temp_hash
                
                if min_possible <= v <= max_possible:
                    S[i] = str(digit)
                    current_hash = temp_hash
                    power = (power * x) % m
                    break
            else:
                result = 'NO SOLUTION'
                break
        else:
            if current_hash == v:
                result = ''.join(S)
            else:
                result = 'NO SOLUTION'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
