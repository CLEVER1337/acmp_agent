
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = []
    B = []
    index = 1
    for i in range(n):
        A.append(int(data[index]))
        B.append(int(data[index+1]))
        index += 2
        
    total_diff = 0
    diffs = []
    for i in range(n):
        total_diff += A[i] + B[i]
        diffs.append((A[i] + B[i], A[i], B[i]))
        
    diffs.sort(key=lambda x: x[0], reverse=True)
    
    player1_score = 0
    player2_score = 0
    
    for i in range(n):
        if i % 2 == 0:
            player1_score += diffs[i][1]
        else:
            player2_score += diffs[i][2]
            
    result = player1_score - player2_score
    print(result)

if __name__ == "__main__":
    main()
