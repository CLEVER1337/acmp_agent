
def generate_darts():
    singles = [str(i) for i in range(1, 21)]
    doubles = ['D' + str(i) for i in range(1, 21)]
    triples = ['T' + str(i) for i in range(1, 21)]
    bullseye = ['25', 'Bull']
    return singles + doubles + triples + bullseye

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
    darts = generate_darts()
    results = []
    
    for dart1 in darts:
        score1 = get_score(dart1)
        if score1 == n and dart1.startswith(('D', 'Bull')) or dart1 == '25':
            results.append([dart1])
        
        for dart2 in darts:
            score2 = get_score(dart2)
            total = score1 + score2
            if total == n and (dart2.startswith(('D', 'Bull')) or dart2 == '25'):
                results.append([dart1, dart2])
            
            for dart3 in darts:
                score3 = get_score(dart3)
                total = score1 + score2 + score3
                if total == n and (dart3.startswith(('D', 'Bull')) or dart3 == '25'):
                    results.append([dart1, dart2, dart3])
    
    results.sort(key=lambda x: (len(x), x[0] if x else '', x[1] if len(x) > 1 else '', x[2] if len(x) > 2 else ''))
    
    print(len(results))
    for res in results:
        print(' '.join(res))

if __name__ == '__main__':
    main()
