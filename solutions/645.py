
import math

def main():
    K = int(input().strip())
    best_h = 1
    best_w = K
    min_beauty = float('inf')
    
    for h in range(1, int(math.isqrt(K)) + 1):
        if K % h == 0:
            w = K // h
            beauty = abs(h - w) + (h + w - 2)
            if beauty < min_beauty:
                min_beauty = beauty
                best_h, best_w = h, w
            elif beauty == min_beauty:
                if h < best_h:
                    best_h, best_w = h, w
    
    print(f"{best_h} {best_w}")

if __name__ == "__main__":
    main()
