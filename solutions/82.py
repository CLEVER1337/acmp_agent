
def solve():
    with open('INPUT.TXT', 'r') as file:
        N, M = map(int, file.readline().split())
        set1 = set(map(int, file.readline().split()))
        set2 = set(map(int, file.readline().split()))
    
    common_elements = sorted(set1 & set2)
    
    with open('OUTPUT.TXT', 'w') as file:
        file.write(' '.join(map(str, common_elements)))
        
solve()
