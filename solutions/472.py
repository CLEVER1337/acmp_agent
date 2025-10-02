
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    gifts = list(map(int, data[2:2+n]))
    
    gifts.sort()
    
    for _ in range(m):
        gifts[0] += 1
        gifts.sort()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(gifts[0]))

if __name__ == "__main__":
    main()
