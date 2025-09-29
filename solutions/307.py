
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    performances = []
    index = 3
    for i in range(p):
        athlete = int(data[index])
        exercise = int(data[index + 1])
        index += 2
        performances.append((athlete, exercise))
    
    count = 0
    for i in range(len(performances)):
        current_athlete, current_exercise = performances[i]
        for j in range(i):
            prev_athlete, prev_exercise = performances[j]
            if current_athlete > prev_athlete and current_exercise < prev_exercise:
                count += 1
            elif current_athlete < prev_athlete and current_exercise > prev_exercise:
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()
