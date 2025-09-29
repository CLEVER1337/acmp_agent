
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        rolls = list(map(int, f.readline().split()))
    
    score = 0
    frame = 0
    i = 0
    
    while frame < 10:
        if rolls[i] == 10:  # Strike
            score += 10 + rolls[i+1] + rolls[i+2]
            i += 1
            frame += 1
        elif i + 1 < len(rolls) and rolls[i] + rolls[i+1] == 10:  # Spare
            score += 10 + rolls[i+2]
            i += 2
            frame += 1
        else:
            score += rolls[i] + rolls[i+1]
            i += 2
            frame += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(score))

if __name__ == '__main__':
    main()
