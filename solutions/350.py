
from itertools import permutations

def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    perms = sorted(set([''.join(p) for p in permutations(s)]))
    
    with open('OUTPUT.TXT', 'w') as f:
        for p in perms:
            f.write(p + '\n')

if __name__ == '__main__':
    main()
