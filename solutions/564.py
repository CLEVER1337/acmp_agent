
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    lengths = list(map(int, data[1:1+n]))
    
    if n < 3:
        print(-1)
        return
        
    lengths_sorted = sorted(lengths, reverse=True)
    
    max_area = -1
    best_triplet_indices = []
    
    for i in range(n - 2):
        a = lengths_sorted[i]
        b = lengths_sorted[i + 1]
        c = lengths_sorted[i + 2]
        
        if a < b + c:
            p = (a + b + c) / 2.0
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            if area > max_area:
                max_area = area
                best_triplet = [a, b, c]
    
    if max_area <= 0:
        print(-1)
        return
        
    original_indices = []
    used = set()
    
    for length in best_triplet:
        for idx, val in enumerate(lengths):
            if val == length and idx not in used:
                original_indices.append(idx + 1)
                used.add(idx)
                break
    
    print("{:.6f}".format(max_area))
    print(" ".join(map(str, original_indices)))

if __name__ == "__main__":
    main()
