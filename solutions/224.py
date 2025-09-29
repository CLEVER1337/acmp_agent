
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    numbers = list(map(int, data[1:1+n]))
    
    numbers.sort()
    
    # Рассматриваем два варианта: три самых больших числа или два самых маленьких и одно самое большое
    candidate1 = numbers[-1] * numbers[-2] * numbers[-3]
    candidate2 = numbers[0] * numbers[1] * numbers[-1]
    
    result = max(candidate1, candidate2)
    print(result)

if __name__ == "__main__":
    main()
