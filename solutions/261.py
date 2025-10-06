
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m, k = map(int, data[0].split())
    A = list(map(int, data[1].split()))
    numbers = []
    for i in range(2, 2 + n):
        numbers.append(data[i].strip())
    
    trie = {}
    for num in numbers:
        node = trie
        for digit in num:
            d = int(digit)
            if d not in node:
                node[d] = {'count': 0}
            node = node[d]
            node['count'] = node.get('count', 0) + 1
    
    min_total = float('inf')
    
    def dfs(node, depth, current_sum):
        nonlocal min_total
        if depth == m:
            total = current_sum
            if total < min_total:
                min_total = total
            return
        
        for digit in range(k):
            if digit not in node:
                continue
                
            child_node = node[digit]
            count = child_node['count']
            cost = A[depth] * count
            dfs(child_node, depth + 1, current_sum + cost)
    
    dfs(trie, 0, 0)
    print(min_total)

if __name__ == "__main__":
    main()
