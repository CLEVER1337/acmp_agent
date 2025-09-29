
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].split()
    P = int(first_line[0])
    N = int(first_line[1])
    K = int(first_line[2])
    
    universities = []
    for i in range(1, 1 + P):
        universities.append(data[i].strip())
    
    team_ids = []
    if len(data) > 1 + P:
        team_ids_line = data[1 + P].split()
        team_ids = [int(x) for x in team_ids_line]
    else:
        team_ids = list(range(1, P + 1))
    
    university_count = {}
    selected_teams = []
    
    for place in range(P):
        university = universities[place]
        team_id = team_ids[place]
        
        current_count = university_count.get(university, 0)
        if current_count < K:
            selected_teams.append((place + 1, university, team_id))
            university_count[university] = current_count + 1
            
            if len(selected_teams) == N:
                break
    
    selected_teams.sort(key=lambda x: x[0])
    
    for place, university, team_id in selected_teams:
        print(f"{university} #{team_id}")

if __name__ == "__main__":
    main()
