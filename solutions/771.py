
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    p = int(data[0])
    edges = []
    nodes = set()
    children_map = {}
    parent_map = {}
    
    for i in range(1, p+1):
        parts = data[i].split()
        if len(parts) < 2:
            continue
        child, parent = parts[0], parts[1]
        nodes.add(child)
        nodes.add(parent)
        edges.append((child, parent))
        if parent not in children_map:
            children_map[parent] = []
        children_map[parent].append(child)
        parent_map[child] = parent
    
    roots = []
    for node in nodes:
        if node not in parent_map or parent_map[node] == '-':
            roots.append(node)
    
    roots.sort()
    
    fc = {}
    ns = {}
    
    for parent in children_map:
        children = children_map[parent]
        children.sort()
        fc[parent] = children[0] if children else None
        for i in range(len(children)):
            if i < len(children) - 1:
                ns[children[i]] = children[i+1]
            else:
                ns[children[i]] = None
    
    output_lines = []
    visited = set()
    
    def build_tree(root):
        stack = [(root, 0)]
        lines = []
        while stack:
            node, level = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            
            prefix = "  " * level
            line = prefix + node
            lines.append(line)
            
            if node in fc and fc[node]:
                stack.append((fc[node], level + 1))
            if node in ns and ns[node]:
                stack.append((ns[node], level))
        return lines
    
    for root in roots:
        output_lines.extend(build_tree(root))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
