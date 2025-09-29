
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        cards = list(map(int, f.readline().split()))
    
    cards.sort()
    total = sum(cards)
    player_sum = sum(cards[i] for i in range(n-1, n//2 - 1, -1))
    result = 2 * player_sum - total
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
