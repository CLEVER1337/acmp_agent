
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n = int(data[0])
    edges = []
    nodes = set()
    parent_map = {}
    children_map = {}
    
    for i in range(1, n + 1):
        if data[i].strip():
            child, parent = data[i].split()
            edges.append((child, parent))
            nodes.add(child)
            nodes.add(parent)
            parent_map[child] = parent
            if parent not in children_map:
                children_map[parent] = []
            children_map[parent].append(child)
    
    roots = []
    for node in nodes:
        if node not in parent_map or parent_map[node] == '-':
            roots.append(node)
    
    roots.sort()
    
    fc_map = {}
    ns_map = {}
    
    for parent in children_map:
        children = children_map[parent]
        children.sort()
        fc_map[parent] = children[0] if children else None
        for i in range(len(children) - 1):
            ns_map[children[i]] = children[i + 1]
    
    output_lines = []
    visited = set()
    
    def dfs(node, level):
        if node in visited:
            return
        visited.add(node)
        
        prefix = "|   " * level
        output_lines.append(f"{prefix}+---{node}")
        
        first_child = fc_map.get(node)
        if first_child:
            dfs(first_child, level + 1)
        
        next_sibling = ns_map.get(node)
        if next_sibling:
            dfs(next_sibling, level)
    
    for root in roots:
        dfs(root, 0)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
