
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    coords = list(map(int, data[2:2+n]))
    
    students = sorted([(coords[i], i) for i in range(n)])
    
    tickets = [0] * n
    colors = []
    left = 0
    
    for pos, idx in students:
        while left < len(colors) and colors[left][0] + d < pos:
            left += 1
        
        if left < len(colors):
            ticket = colors[left][1]
            colors[left] = (pos, ticket)
            tickets[idx] = ticket
        else:
            ticket = len(colors) + 1
            colors.append((pos, ticket))
            tickets[idx] = ticket
    
    print(len(colors))
    print(' '.join(map(str, tickets)))

if __name__ == "__main__":
    main()
