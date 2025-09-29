
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    temperatures = list(map(int, data[1:1+n]))
    
    temperatures.sort()
    
    print(' '.join(map(str, temperatures)))

if __name__ == "__main__":
    main()
