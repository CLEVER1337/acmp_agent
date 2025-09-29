
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
        s = f.readline().strip()
    
    words = set()
    for i in range(len(s) - m + 1):
        words.add(s[i:i+m])
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(len(words)))

if __name__ == "__main__":
    main()
