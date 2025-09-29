
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    current_patrons = []
    for _ in range(n):
        current_patrons.append(int(data[idx])); idx += 1
        
    m = int(data[idx]); idx += 1
    requests = {}
    for _ in range(m):
        current = int(data[idx]); idx += 1
        desired = int(data[idx]); idx += 1
        requests[current] = desired
        
    final_patron = {}
    for patron in set(current_patrons):
        visited = set()
        current = patron
        while current in requests and current not in visited:
            visited.add(current)
            current = requests[current]
        final_patron[patron] = current
        
    result = []
    for patron in current_patrons:
        result.append(str(final_patron.get(patron, patron)))
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    main()
