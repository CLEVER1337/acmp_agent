
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    people = []
    index = 1
    for i in range(n):
        t_i = int(data[index])
        w_i = int(data[index + 1])
        index += 2
        people.append((t_i, w_i, i))
    
    groups = []
    current_max_t = 0
    group_start = 0
    
    for i in range(n):
        if people[i][0] > current_max_t:
            current_max_t = people[i][0]
        if i == n - 1 or people[i + 1][0] < current_max_t:
            groups.append((group_start, i))
            group_start = i + 1
            current_max_t = 0
    
    result = [0] * n
    total_time = 0
    prev_end = n
    
    for start, end in reversed(groups):
        group_people = people[start:end + 1]
        max_t = max(t for t, w, idx in group_people)
        total_steps = 0
        for i in range(start, prev_end):
            total_steps = max(total_steps, people[i][1])
        total_time += max_t * total_steps
        for i in range(start, end + 1):
            result[people[i][2]] = total_time
        prev_end = start
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
