
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    children = {}
    parent_map = {}
    values = {}
    is_leaf = {}
    
    for i in range(1, n):
        parts = data[i].split()
        node_type = parts[0]
        parent = int(parts[1])
        node_id = i + 1
        
        if node_type == 'L':
            value = int(parts[2])
            values[node_id] = value
            is_leaf[node_id] = True
        else:
            is_leaf[node_id] = False
        
        if parent not in children:
            children[parent] = []
        children[parent].append(node_id)
        parent_map[node_id] = parent
    
    result = {}
    stack = [1]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node in children:
            for child in reversed(children[node]):
                stack.append(child)
    
    for node in reversed(order):
        if is_leaf.get(node, False):
            result[node] = values[node]
        else:
            child_nodes = children.get(node, [])
            if not child_nodes:
                result[node] = 0
            else:
                if node == 1:
                    current_player = 1
                else:
                    parent = parent_map[node]
                    depth_diff = 0
                    temp = node
                    while temp != 1:
                        temp = parent_map[temp]
                        depth_diff += 1
                    current_player = 1 if depth_diff % 2 == 0 else -1
                
                child_results = [result[child] for child in child_nodes]
                if current_player == 1:
                    res = max(child_results)
                else:
                    res = min(child_results)
                result[node] = res
    
    print(result[1])

if __name__ == "__main__":
    main()
