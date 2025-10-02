
def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.readline().strip())
    
    max_received = 0
    min_cost = float('inf')
    
    for amount in range(N, 0, -1):
        cost = (amount + 99) // 100 * 7
        if amount + cost <= N:
            if amount > max_received:
                max_received = amount
                min_cost = cost
            elif amount == max_received and cost < min_cost:
                min_cost = cost
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{max_received} {min_cost}")

if __name__ == "__main__":
    main()
