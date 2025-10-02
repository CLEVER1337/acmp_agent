
def main():
    with open('INPUT.TXT', 'r') as f:
        kirill = f.readline().strip()
        dima = f.readline().strip()
    
    if len(kirill) != len(dima):
        print(-1)
        return
        
    if kirill == dima:
        print(0)
        return
        
    double = kirill + kirill
    pos = double.find(dima)
    
    if pos == -1:
        print(-1)
    else:
        print(pos)

if __name__ == "__main__":
    main()
