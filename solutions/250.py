
def is_dvoyakoe(n):
    s = str(n)
    return len(set(s)) <= 2

def find_closest_dvoyakoe(N):
    if is_dvoyakoe(N):
        return N
        
    lower = N - 1
    while lower >= 1:
        if is_dvoyakoe(lower):
            break
        lower -= 1
            
    higher = N + 1
    while higher <= 30000:
        if is_dvoyakoe(higher):
            break
        higher += 1
            
    if lower < 1:
        return higher
    if higher > 30000:
        return lower
        
    dist_lower = N - lower
    dist_higher = higher - N
    
    if dist_lower < dist_higher:
        return lower
    elif dist_higher < dist_lower:
        return higher
    else:
        return lower

with open('INPUT.TXT', 'r') as f:
    N = int(f.read().strip())
    
result = find_closest_dvoyakoe(N)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
