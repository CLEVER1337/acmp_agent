
def read_input():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    templates = {}
    for _ in range(M):
        template_id = int(data[idx]); idx += 1
        heights = list(map(int, data[idx:idx+L]))
        idx += L
        templates[template_id] = heights
    
    sections = []
    for _ in range(N):
        heights = list(map(int, data[idx:idx+L]))
        idx += L
        sections.append(heights)
    
    return L, M, N, templates, sections

def normalize_section(section):
    min_val = min(section)
    normalized = [h - min_val for h in section]
    return normalized

def match_section(section, templates):
    normalized_section = normalize_section(section)
    
    best_match_id = None
    best_diff = float('inf')
    
    for template_id, template_heights in templates.items():
        normalized_template = normalize_section(template_heights)
        
        diff = sum(abs(a - b) for a, b in zip(normalized_section, normalized_template))
        
        if diff < best_diff:
            best_diff = diff
            best_match_id = template_id
    
    return best_match_id if best_diff == 0 else '-'

def main():
    L, M, N, templates, sections = read_input()
    
    results = []
    matched_count = 0
    bad_count = 0
    
    for section in sections:
        result = match_section(section, templates)
        results.append(str(result))
        
        if result == '-':
            bad_count += 1
        else:
            matched_count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        for result in results:
            f.write(result + '\n')
        f.write(f'OK= {matched_count} BAD= {bad_count}\n')

if __name__ == '__main__':
    main()
