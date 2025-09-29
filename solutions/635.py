
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    base_teams = []
    for i in range(n):
        team_id = int(data[index])
        solved = int(data[index+1])
        penalty = int(data[index+2])
        index += 3
        base_teams.append((team_id, solved, penalty))
    
    advanced_teams = []
    for i in range(m):
        team_id = int(data[index])
        solved = int(data[index+1])
        penalty = int(data[index+2])
        index += 3
        advanced_teams.append((team_id, solved, penalty))
    
    # Сортируем базовые команды по убыванию решенных задач, возрастанию штрафа
    base_teams_sorted = sorted(base_teams, key=lambda x: (-x[1], x[2]))
    
    # Сортируем усложненные команды по убыванию решенных задач, возрастанию штрафа
    advanced_teams_sorted = sorted(advanced_teams, key=lambda x: (-x[1], x[2]))
    
    # Определяем количество команд для перехода из базовой в усложненную
    if n >= 12:
        teams_to_advance = base_teams_sorted[:12]
    else:
        teams_to_advance = base_teams_sorted[:]
    
    # Определяем количество команд для вылета из усложненной в базовую
    if m >= 12:
        teams_to_demote = advanced_teams_sorted[12:]
    else:
        teams_to_demote = []
    
    # Формируем итоговый список для усложненной номинации
    # Все команды из усложненной номинации, кроме вылетающих
    final_advanced = []
    for team in advanced_teams_sorted:
        if team not in teams_to_demote:
            final_advanced.append(team[0])
    
    # Добавляем команды, переходящие из базовой в усложненную
    for team in teams_to_advance:
        final_advanced.append(team[0])
    
    # Сортируем идентификаторы по возрастанию
    final_advanced_sorted = sorted(final_advanced)
    
    # Выводим результат
    print(len(final_advanced_sorted))
    print(" ".join(map(str, final_advanced_sorted)))

if __name__ == "__main__":
    main()
