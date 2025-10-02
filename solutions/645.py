
import math

def main():
    k = int(input().strip())
    best_h = 1
    best_w = k
    best_score = float('inf')
    
    for h in range(1, int(math.isqrt(k)) + 1):
        if k % h == 0:
            w = k // h
            unused = k - h * w
            diff = abs(h - w)
            score = unused + diff
            if score < best_score or (score == best_score and h <= best_h):
                best_score = score
                best_h = h
                best_w = w
    
    print(f"{best_h} {best_w}")

if __name__ == "__main__":
    main()
