
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    
    base_teams = []
    for i in range(1, 1 + n):
        parts = data[i].split()
        id_val = int(parts[0])
        s_val = int(parts[1])
        t_val = int(parts[2])
        base_teams.append((id_val, s_val, t_val))
    
    advanced_teams = []
    for i in range(1 + n, 1 + n + m):
        parts = data[i].split()
        id_val = int(parts[0])
        s_val = int(parts[1])
        t_val = int(parts[2])
        advanced_teams.append((id_val, s_val, t_val))
    
    all_teams = base_teams + advanced_teams
    all_teams.sort(key=lambda x: (-x[1], x[2], x[0]))
    
    advanced_next = set()
    count = 0
    for team in all_teams:
        if count < 12:
            advanced_next.add(team[0])
            count += 1
        else:
            break
    
    for team in advanced_teams:
        if team[1] > 0:
            advanced_next.add(team[0])
    
    result = sorted(advanced_next)
    print(len(result))
    if result:
        print(" ".join(map(str, result)))
    else:
        print()

if __name__ == "__main__":
    main()
