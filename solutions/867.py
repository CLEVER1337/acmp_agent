
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    D = int(data[1])
    coords = list(map(int, data[2:2+n]))
    
    students = sorted([(coords[i], i) for i in range(n)])
    
    tickets = [0] * n
    colors = []
    left = 0
    color_count = 0
    
    for right in range(n):
        while students[right][0] - students[left][0] > D:
            left += 1
        
        if not colors or len(colors) == 0:
            color_count += 1
            colors.append(color_count)
            tickets[students[right][1]] = color_count
        else:
            available = set(range(1, color_count + 1))
            for i in range(left, right):
                if students[right][0] - students[i][0] <= D:
                    if tickets[students[i][1]] in available:
                        available.remove(tickets[students[i][1]])
            
            if available:
                chosen = min(available)
                tickets[students[right][1]] = chosen
            else:
                color_count += 1
                tickets[students[right][1]] = color_count
                colors.append(color_count)
    
    print(color_count)
    print(" ".join(map(str, tickets)))

if __name__ == "__main__":
    main()
