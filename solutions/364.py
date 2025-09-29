
def main():
    with open("INPUT.TXT", "r") as f:
        M, N = map(int, f.readline().split())
    
    perfect_numbers = []
    
    # Известные совершенные числа в диапазоне до 5*10^18
    known_perfects = [
        6,
        28,
        496,
        8128,
        33550336,
        8589869056,
        137438691328,
        2305843008139952128
    ]
    
    for num in known_perfects:
        if M <= num <= N:
            perfect_numbers.append(num)
    
    perfect_numbers.sort()
    
    with open("OUTPUT.TXT", "w") as f:
        if perfect_numbers:
            for num in perfect_numbers:
                f.write(f"{num}\n")
        else:
            f.write("Absent\n")

if __name__ == "__main__":
    main()
