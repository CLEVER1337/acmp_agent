
def count_fives(n):
    count = 0
    power_of_10 = 1
    
    while power_of_10 <= n:
        higher = n // (power_of_10 * 10)
        current_digit = (n // power_of_10) % 10
        lower = n % power_of_10
        
        if current_digit < 5:
            count += higher * power_of_10
        elif current_digit == 5:
            count += higher * power_of_10 + lower + 1
        else:
            count += (higher + 1) * power_of_10
        
        power_of_10 *= 10
    
    return count

with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    
result = count_fives(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
