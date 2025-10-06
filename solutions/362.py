
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    a, b = map(int, lines[0].split())
    c, d = map(int, lines[1].split())
    
    if (a <= c and b <= d) or (a <= d and b <= c):
        result = "Possible"
    else:
        result = "Impossible"
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
