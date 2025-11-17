
import sys

def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    if m == 1:
        print(n)
        return
        
    total_eliminated = 0
    current_round = 1
    remaining = n
    eliminated_in_round = 0
    
    while True:
        if remaining == 1:
            break
            
        if remaining % 2 == 0:
            eliminated_in_round = remaining // 2
        else:
            eliminated_in_round = (remaining - 1) // 2
            
        if m % 2 == 0:
            eliminated_position = (m // 2)
            total_eliminated += eliminated_position
            print(total_eliminated)
            return
            
        total_eliminated += eliminated_in_round
        if remaining % 2 == 0:
            remaining //= 2
        else:
            remaining = (remaining + 1) // 2
        m = (m + 1) // 2
        
    print(n)

if __name__ == "__main__":
    main()
