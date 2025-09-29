
import sys
from math import comb

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        K = int(data[1])
        M = int(data[2])
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'[:N]
    result = []
    m = M - 1
    
    for i in range(K):
        for j in range(len(alphabet)):
            remaining = K - len(result) - 1
            if remaining < 0:
                break
            count = comb(len(alphabet) - j - 1, remaining)
            if m < count:
                result.append(alphabet[j])
                alphabet = alphabet[j+1:]
                break
            else:
                m -= count
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
