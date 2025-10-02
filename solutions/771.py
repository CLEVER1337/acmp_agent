
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
        parts = data[i].split()
        if len(parts) < 2:
            continue
        child, parent = parts[0], parts[1]
        nodes.add(child)
        nodes.add(parent)
        edges.append((child, parent))
        parent_map[child] = parent
        if parent != '-':
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
        for i in range(len(children)):
            if i < len(children) - 1:
                ns_map[children[i]] = children[i + 1]
            else:
                ns_map[children[i]] = None
    
    output_lines = []
    output_lines.append(''.join(roots))
    
    visited = set()
    stack = []
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        stack.append(node)
        
        line_parts = []
        for n in stack[:-1]:
            if ns_map.get(n, None) is not None:
                line_parts.append('|')
            else:
                line_parts.append(' ')
            line_parts.append(' ')
        
        if stack:
            line_parts.append('+--')
        line_parts.append(node)
        output_lines.append(''.join(line_parts))
        
        if node in fc_map and fc_map[node] is not None:
            dfs(fc_map[node])
        
        if node in ns_map and ns_map[node] is not None:
            stack.pop()
            dfs(ns_map[node])
        else:
            stack.pop()
    
    for root in roots:
        dfs(root)
    
    with open('OUTPUT.TXT', 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

if __name__ == '__main__':
    main()
