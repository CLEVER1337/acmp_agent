
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    permutation = list(map(int, data[1].split()))
    
    inverse = [0] * n
    for i in range(n):
        value = permutation[i]
        inverse[value - 1] = i + 1
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, inverse)))

if __name__ == '__main__':
    main()
