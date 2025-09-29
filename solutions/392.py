
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    
    min_val = min(p)
    indices = [i for i, x in enumerate(p) if x == min_val]
    
    best_start = indices[0]
    for idx in indices[1:]:
        k = 1
        while k < n:
            pos1 = (best_start + k) % n
            pos2 = (idx + k) % n
            if p[pos1] < p[pos2]:
                break
            elif p[pos1] > p[pos2]:
                best_start = idx
                break
            k += 1
    
    result = p[best_start:] + p[:best_start]
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
