
def process_deck(n):
    steps = 0
    while n != 2:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    with open('INPUT.TXT', 'r') as f:
        p, k = map(int, f.read().split())
    
    total_steps = 0
    for cards in range(p, k + 1):
        try:
            steps = process_deck(cards)
            total_steps += steps
        except:
            total_steps = 0
            break
    
    print(total_steps)

if __name__ == '__main__':
    main()
