
def main():
    with open("INPUT.TXT", "r") as f:
        x, y = map(int, f.readline().split())
    
    if x == 1 and y == 1:
        print(0)
        return
        
    if (x - 1) ^ (y - 1) == 0:
        print(2)
    else:
        print(1)

if __name__ == "__main__":
    main()
