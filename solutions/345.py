
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    n = int(data[0])
    index = 1
    procedures = {}
    proc_list = []
    
    for _ in range(n):
        proc_id = data[index]
        index += 1
        k = int(data[index])
        index += 1
        calls = []
        for i in range(k):
            calls.append(data[index])
            index += 1
        procedures[proc_id] = calls
        proc_list.append(proc_id)
        index += 1  # Skip the "*****" line
    
    graph = {}
    for proc in procedures:
        graph[proc] = procedures[proc]
    
    def is_recursive(start):
        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node == start and visited:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    stack.append(neighbor)
        return False
    
    result = []
    for proc in proc_list:
        if is_recursive(proc):
            result.append("YES")
        else:
            result.append("NO")
    
    with open('OUTPUT.TXT', 'w') as f:
        for res in result:
            f.write(res + '\n')

if __name__ == "__main__":
    main()
