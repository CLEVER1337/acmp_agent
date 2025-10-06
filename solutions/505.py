
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    L = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    templates = {}
    for _ in range(M):
        num = int(data[idx]); idx += 1
        heights = list(map(int, data[idx:idx+L]))
        idx += L
        templates[num] = heights
    
    sections = []
    for _ in range(N):
        heights = list(map(int, data[idx:idx+L]))
        idx += L
        sections.append(heights)
    
    results = []
    matched_count = 0
    
    for sec in sections:
        found = False
        for t_num, t_heights in templates.items():
            match = True
            for i in range(L):
                if sec[i] != t_heights[i]:
                    match = False
                    break
            if match:
                results.append(str(t_num))
                matched_count += 1
                found = True
                break
        
        if not found:
            results.append('-')
    
    for res in results:
        print(res)
    
    bad_count = N - matched_count
    print(f"OK= {matched_count} BAD= {bad_count}")

if __name__ == "__main__":
    main()
