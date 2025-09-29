
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    players = []
    index = 1
    for i in range(n):
        a1 = int(data[index])
        a2 = int(data[index+1])
        a3 = int(data[index+2])
        index += 3
        players.append((a1, a2, a3))
    
    results = set()
    for p in range(0, 101):
        total_scores = []
        for player in players:
            a1, a2, a3 = player
            if a1 == p:
                score1 = 0
            else:
                score1 = a1
                
            if a2 == p:
                score2 = 0
            else:
                score2 = a2
                
            if a3 == p:
                score3 = 0
            else:
                score3 = a3
                
            total_score = score1 + score2 + score3
            total_scores.append(total_score)
        
        total_scores.sort()
        results.add(tuple(total_scores))
    
    print(len(results))

if __name__ == "__main__":
    main()
