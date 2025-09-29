
def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.read().strip())
    
    target = 2 * N
    queue = []
    visited_remainders = set()
    
    queue.append((1, "1"))
    queue.append((2, "2"))
    visited_remainders.add(1)
    visited_remainders.add(2)
    
    while queue:
        remainder, number_str = queue.pop(0)
        
        if remainder % target == 0:
            with open("OUTPUT.TXT", "w") as f:
                f.write(number_str)
            return
        
        for digit in [1, 2]:
            new_remainder = (remainder * 10 + digit) % target
            if new_remainder not in visited_remainders:
                visited_remainders.add(new_remainder)
                new_number_str = number_str + str(digit)
                if len(new_number_str) <= 10000:
                    queue.append((new_remainder, new_number_str))

if __name__ == "__main__":
    main()
