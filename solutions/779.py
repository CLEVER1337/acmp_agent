
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    houses = list(map(int, data[1:1+n]))
    
    median_index = (n - 1) // 2
    result = houses[median_index]
    
    print(result)

if __name__ == "__main__":
    main()
