
def main():
    with open("INPUT.TXT", "r") as f:
        N, M, K = map(int, f.readline().split())
    
    if M < 2 * ((N + K - 1) // K):
        print(0)
        return
        
    total_people = N + M
    buses = (total_people + K - 1) // K
    
    if buses * K - M < N:
        buses += 1
        
    if buses * K - M < N or M < 2 * ((N + buses - 1) // buses):
        print(0)
    else:
        print(buses)

if __name__ == "__main__":
    main()
