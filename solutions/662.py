
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
            if p == 0:
                total = a1 + a2 + a3
            else:
                total = (a1 + a2 + a3) % p
            total_scores.append(total)
        
        sorted_scores = tuple(sorted(total_scores))
        results.add(sorted_scores)
    
    print(len(results))

if __name__ == "__main__":
    main()
