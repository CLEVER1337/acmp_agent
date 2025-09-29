
def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.readline().strip())
    
    if N <= 1:
        print("Stan wins.")
        return
        
    p = 1
    while p < N:
        p *= 9
        if p >= N:
            print("Stan wins.")
            return
        p *= 2
        if p >= N:
            print("Ollie wins.")
            return

if __name__ == "__main__":
    main()
