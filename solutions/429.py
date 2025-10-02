
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        nodes = {}
        children = {}
        
        for i in range(2, n + 1):
            line = f.readline().split()
            node_type = line[0]
            parent = int(line[1])
            
            if node_type == 'L':
                value = int(line[2])
                nodes[i] = {'type': 'leaf', 'value': value}
            else:
                nodes[i] = {'type': 'internal'}
                if parent not in children:
                    children[parent] = []
                children[parent].append(i)
    
    result = {}
    
    def dfs(node):
        if node in result:
            return result[node]
            
        if nodes[node]['type'] == 'leaf':
            result[node] = nodes[node]['value']
            return result[node]
            
        if node not in children:
            return 0
            
        child_values = [dfs(child) for child in children[node]]
        
        if node == 1:
            result[node] = max(child_values)
        else:
            level = 1
            temp = node
            while temp != 1:
                level += 1
                for p, kids in children.items():
                    if temp in kids:
                        temp = p
                        break
            
            if level % 2 == 1:
                result[node] = max(child_values)
            else:
                result[node] = min(child_values)
                
        return result[node]
    
    outcome = dfs(1)
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(outcome))

if __name__ == "__main__":
    main()
