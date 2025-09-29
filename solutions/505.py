
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    L = int(data[0])
    M = int(data[1])
    N = int(data[2])
    
    templates = {}
    index = 3
    
    for _ in range(M):
        template_id = int(data[index])
        heights = list(map(int, data[index+1:index+1+L]))
        templates[template_id] = heights
        index += 1 + L
    
    sections = []
    for _ in range(N):
        heights = list(map(int, data[index:index+L]))
        sections.append(heights)
        index += L
    
    results = []
    matched_count = 0
    
    for section in sections:
        found = False
        for template_id, template_heights in templates.items():
            if len(section) != len(template_heights):
                continue
                
            match = True
            for i in range(L):
                if section[i] != template_heights[i]:
                    match = False
                    break
            
            if match:
                results.append(str(template_id))
                matched_count += 1
                found = True
                break
        
        if not found:
            results.append('-')
    
    bad_count = N - matched_count
    
    for res in results:
        print(res)
    
    print(f"OK= {matched_count} BAD= {bad_count}")

if __name__ == "__main__":
    main()
