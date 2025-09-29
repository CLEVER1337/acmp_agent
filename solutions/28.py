
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    
    x1, y1, x2, y2 = map(int, data[:4])
    xA, yA = map(int, data[4:6])
    
    if x1 == x2:
        xB = 2 * x1 - xA
        yB = yA
    else:
        xB = xA
        yB = 2 * y1 - yA
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{xB} {yB}")

if __name__ == "__main__":
    main()
