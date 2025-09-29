
import math

def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.readline().strip())
    
    if N <= 2:
        result = 1
    else:
        k = 0
        while (3 ** k) < N:
            k += 1
        result = k
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
