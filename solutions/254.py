
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    current_patrons = list(map(int, data[idx:idx+n]))
    idx += n
    
    m = int(data[idx]); idx += 1
    requests = {}
    for _ in range(m):
        current = int(data[idx]); idx += 1
        desired = int(data[idx]); idx += 1
        requests[current] = desired
    
    patron_map = {}
    for i in range(1, 201):
        patron_map[i] = i
    
    for current, desired in requests.items():
        patron_map[current] = desired
    
    final_patrons = []
    for patron in current_patrons:
        while patron != patron_map[patron]:
            patron = patron_map[patron]
        final_patrons.append(patron)
    
    with open('OUTPUT.TXT', 'w') as f:
        for p in final_patrons:
            f.write(f"{p}\n")

if __name__ == "__main__":
    main()
