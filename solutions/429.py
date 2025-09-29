
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        nodes = {}
        children = {}
        
        for i in range(2, n + 1):
            line = f.readline().strip().split()
            node_type = line[0]
            parent = int(line[1])
            
            if parent not in children:
                children[parent] = []
            children[parent].append(i)
            
            if node_type == 'L':
                value = int(line[2])
                nodes[i] = {'type': 'leaf', 'value': value}
            else:
                nodes[i] = {'type': 'internal'}
    
    result = {}
    
    def dfs(node):
        if node in result:
            return result[node]
            
        if node not in children:
            return nodes[node]['value']
            
        child_values = []
        for child in children[node]:
            child_values.append(dfs(child))
            
        if len(child_values) == 0:
            return nodes[node]['value']
            
        if node == 1:
            result[node] = max(child_values)
        else:
            result[node] = min(child_values)
            
        return result[node]
    
    root_result = dfs(1)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(root_result))

if __name__ == '__main__':
    main()
