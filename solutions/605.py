
def generate_dart_values():
    values = []
    for i in range(1, 21):
        values.append(str(i))
        values.append('D' + str(i))
        values.append('T' + str(i))
    values.append('25')
    values.append('Bull')
    return values

def get_score(dart):
    if dart == 'Bull':
        return 50
    if dart == '25':
        return 25
    if dart.startswith('D'):
        return 2 * int(dart[1:])
    if dart.startswith('T'):
        return 3 * int(dart[1:])
    return int(dart)

def main():
    n = int(input().strip())
    darts = generate_dart_values()
    results = []
    
    for dart1 in darts:
        score1 = get_score(dart1)
        if score1 == n and dart1.startswith(('D', 'Bull')):
            results.append([dart1])
        if score1 < n:
            for dart2 in darts:
                score2 = get_score(dart2)
                total = score1 + score2
                if total == n and dart2.startswith(('D', 'Bull')):
                    results.append([dart1, dart2])
                if total < n:
                    for dart3 in darts:
                        score3 = get_score(dart3)
                        if total + score3 == n and dart3.startswith(('D', 'Bull')):
                            results.append([dart1, dart2, dart3])
    
    results.sort()
    print(len(results))
    for res in results:
        print(' '.join(res))

if __name__ == '__main__':
    main()
