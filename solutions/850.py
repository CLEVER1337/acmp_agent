
def main():
    a, b = map(int, input().split())
    total_min = float('inf')
    total_max = -1
    n_min = (a + 1) // 2
    n_max = a
    m_min = (b + 1) // 2
    m_max = b
    
    possible_n = set()
    for n in range(n_min, n_max + 1):
        if n == 0:
            continue
        low_legs = 2 * n - a
        if 0 <= low_legs <= n:
            possible_n.add(n)
            
    possible_m = set()
    for m in range(m_min, m_max + 1):
        if m == 0:
            continue
        low_legs = 2 * m - b
        if 0 <= low_legs <= m:
            possible_m.add(m)
            
    common = possible_n & possible_m
    if common:
        total_min = min(common)
        total_max = max(common)
    else:
        for n_val in possible_n:
            for m_val in possible_m:
                total = n_val + m_val - min(n_val, m_val)
                if total_min > total:
                    total_min = total
                if total_max < total:
                    total_max = total
                    
    print(total_min, total_max)

if __name__ == "__main__":
    main()
