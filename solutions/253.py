
def main():
    with open("INPUT.TXT", "r") as f:
        start_h, start_m = map(int, f.readline().split())
        end_h, end_m = map(int, f.readline().split())
    
    total_strikes = 0
    
    current_h = start_h
    current_m = start_m
    
    while (current_h != end_h) or (current_m != end_m):
        if current_m == 0:
            strikes = (current_h - 1) % 12 + 1
            total_strikes += strikes
        elif current_m == 30:
            total_strikes += 1
        
        current_m += 1
        if current_m == 60:
            current_m = 0
            current_h = (current_h + 1) % 24
            
    print(total_strikes, file=open("OUTPUT.TXT", "w"))

if __name__ == "__main__":
    main()
