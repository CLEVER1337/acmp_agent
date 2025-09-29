
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    index = 1
    participants = []
    
    for _ in range(n):
        ni = int(data[index])
        index += 1
        for j in range(ni):
            parts = data[index].split()
            score = float(parts[0])
            name = ' '.join(parts[1:])
            participants.append((score, name))
            index += 1
            
    participants.sort(key=lambda x: (-x[0], x[1]))
    
    total_n = len(participants)
    print(total_n)
    for score, name in participants:
        print(f"{score:.2f} {name}")

if __name__ == "__main__":
    main()
