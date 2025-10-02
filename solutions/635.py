
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    base_teams = []
    for i in range(1, 1 + n):
        parts = data[i].split()
        if len(parts) < 3:
            continue
        team_id = int(parts[0])
        solved = int(parts[1])
        penalty = int(parts[2])
        base_teams.append((team_id, solved, penalty))
        
    advanced_teams = []
    for i in range(1 + n, 1 + n + m):
        parts = data[i].split()
        if len(parts) < 3:
            continue
        team_id = int(parts[0])
        solved = int(parts[1])
        penalty = int(parts[2])
        advanced_teams.append((team_id, solved, penalty))
    
    base_teams_sorted = sorted(base_teams, key=lambda x: (-x[1], x[2]))
    advanced_teams_sorted = sorted(advanced_teams, key=lambda x: (-x[1], x[2]))
    
    advanced_next = set()
    
    if base_teams_sorted:
        top_base_solved = base_teams_sorted[0][1]
        for team in base_teams_sorted:
            if team[1] == top_base_solved:
                advanced_next.add(team[0])
    
    if advanced_teams_sorted:
        for team in advanced_teams_sorted:
            advanced_next.add(team[0])
    
    result_ids = sorted(list(advanced_next))
    
    print(len(result_ids))
    if result_ids:
        print(" ".join(map(str, result_ids)))
    else:
        print()

if __name__ == "__main__":
    main()
