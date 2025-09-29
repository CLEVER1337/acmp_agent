
def main():
    with open('INPUT.TXT', 'r') as f:
        x = float(f.readline().strip())
    
    n = 0
    total = 0.0
    
    while total < x:
        n += 1
        total += 1.0 / (n + 1)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{n} card(s)\n")

if __name__ == "__main__":
    main()
