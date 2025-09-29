
def main():
    with open('INPUT.TXT', 'r') as f:
        X, Y = map(int, f.read().split())
    
    for a in range(1, Y + 1):
        for b in range(1, Y + 1):
            coins = [a, b]
            for year in range(3, X + 1):
                coins.append(coins[year - 3])
            if coins[X - 1] == Y:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write(f"{a} {b}")
                return

if __name__ == "__main__":
    main()
