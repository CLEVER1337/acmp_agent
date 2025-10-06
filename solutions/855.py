
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    m = int(data[1])
    n_list = list(map(int, data[2:2+m]))
    
    a = [1] * k
    prod = 1
    
    for i in range(k):
        while True:
            temp_prod = prod * (a[i] + 1)
            valid = True
            for j in range(m):
                expected = n_list[j]
                if j < temp_prod:
                    if expected != 0:
                        valid = False
                        break
                else:
                    divisor = (j + 1) // temp_prod
                    remainder = (j + 1) % temp_prod
                    count = divisor * a[i] + min(remainder, a[i])
                    if count != expected:
                        valid = False
                        break
            if valid:
                a[i] += 1
                prod = temp_prod
            else:
                break
                
    print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
