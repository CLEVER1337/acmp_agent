
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    names = data[1:1+n]
    
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    edges = defaultdict(int)
    
    for name in names:
        first_char = name[0]
        last_char = name[-1]
        out_degree[first_char] += 1
        in_degree[last_char] += 1
        edges[(first_char, last_char)] += 1
    
    chars = set(in_degree.keys()) | set(out_degree.keys())
    
    components = []
    visited = set()
    
    def dfs(node, component):
        stack = [node]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            component.add(current)
            for neighbor in chars:
                if (current, neighbor) in edges and edges[(current, neighbor)] > 0:
                    stack.append(neighbor)
                if (neighbor, current) in edges and edges[(neighbor, current)] > 0:
                    stack.append(neighbor)
    
    for char in chars:
        if char not in visited:
            component = set()
            dfs(char, component)
            components.append(component)
    
    total_added = 0
    for comp in components:
        comp_chars = comp
        balance_sum = 0
        in_minus_out = []
        
        for char in comp_chars:
            balance = out_degree[char] - in_degree[char]
            in_minus_out.append(balance)
            balance_sum += balance
        
        if balance_sum != 0:
            total_added += abs(balance_sum)
        else:
            has_imbalance = any(b != 0 for b in in_minus_out)
            if has_imbalance:
                total_added += 1
    
    if len(components) > 1:
        total_added += len(components) - 1
    
    print(total_added)

if __name__ == "__main__":
    main()
