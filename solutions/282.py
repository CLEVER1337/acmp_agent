
def main():
    with open('INPUT.TXT', 'r') as f:
        W, H = map(int, f.readline().split())
    
    total = 0
    for w in range(1, W + 1):
        for h in range(1, H + 1):
            rectangles = (W - w + 1) * (H - h + 1)
            total += rectangles
    
    print(total)

if __name__ == '__main__':
    main()
