
def main():
    with open('INPUT.TXT', 'r') as f:
        X, Y = map(int, f.read().split())
    
    for a in range(1, Y + 1):
        for b in range(1, Y + 1):
            years = [a, b]
            for i in range(2, X):
                years.append(years[i-1] + years[i-2])
            if years[X-1] == Y:
                with open('OUTPUT.TXT', 'w') as f_out:
                    f_out.write(f"{a} {b}")
                return

if __name__ == "__main__":
    main()
