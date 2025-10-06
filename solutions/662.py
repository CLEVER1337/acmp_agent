
import sys

def main():
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
    
    possible_sums = set()
    
    for p in range(0, 101):
        valid = True
        total_sum = 0
        
        for player in players:
            a1, a2, a3 = player
            max_score = max(a1, a2, a3)
            min_score = min(a1, a2, a3)
            
            if p < min_score or p > max_score:
                valid = False
                break
                
            total_sum += (a1 + a2 + a3 - min_score - max_score)
            
        if valid:
            possible_sums.add(total_sum)
            
    print(len(possible_sums))

if __name__ == "__main__":
    main()
