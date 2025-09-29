
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.readline().split()
        N = int(data[0])
        M = int(data[1])
    
    if M == 1:
        print(N)
        return
        
    rounds = 0
    current_N = N
    while current_N > 0:
        rounds += 1
        eliminated = (current_N + 1) // 2
        if M % 2 == 0 and M <= current_N:
            position = M // 2
            if position <= eliminated:
                result = sum_eliminated_before_round(N, rounds - 1) + position
                print(result)
                return
        current_N -= eliminated
        
    print(N)

def sum_eliminated_before_round(N, round_num):
    total_eliminated = 0
    current_N = N
    for i in range(round_num):
        eliminated = (current_N + 1) // 2
        total_eliminated += eliminated
        current_N -= eliminated
    return total_eliminated

if __name__ == "__main__":
    main()
