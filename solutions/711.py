
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
        participants = []
        
        for _ in range(n):
            name = f.readline().strip()
            times = list(map(int, f.readline().split()))
            total_time = sum(times)
            participants.append((total_time, name))
    
    min_time = min(participants, key=lambda x: x[0])
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(min_time[1])

if __name__ == '__main__':
    main()
