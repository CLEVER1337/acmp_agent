
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    index = 1
    initial_confed = []
    for i in range(n):
        initial_confed.append(int(data[index]))
        index += 1
        
    m = int(data[index])
    index += 1
    requests = {}
    for i in range(m):
        current = int(data[index])
        desired = int(data[index+1])
        index += 2
        requests[current] = desired
        
    confed_to_priest = {}
    for confed_id, priest in enumerate(initial_confed, 1):
        confed_to_priest[confed_id] = priest
        
    result = []
    for confed_id in range(1, n+1):
        current_priest = confed_to_priest[confed_id]
        visited = set()
        while current_priest in requests and current_priest not in visited:
            visited.add(current_priest)
            current_priest = requests[current_priest]
        result.append(str(current_priest))
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(result))

if __name__ == "__main__":
    main()
