
def main():
    with open("INPUT.TXT", "r") as f:
        c, h, o = map(int, f.readline().split())
    
    molecules = min(c // 2, h // 6, o)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(molecules))

if __name__ == "__main__":
    main()
