
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m, k = map(int, data[0].split())
    A = list(map(int, data[1].split()))
    bets = []
    for i in range(2, 2 + n):
        line = data[i].strip()
        if line:
            bets.append(line)
    
    prefix_tree = {}
    for bet in bets:
        node = prefix_tree
        for char in bet:
            digit = int(char)
            if digit not in node:
                node[digit] = {'count': 0}
            node = node[digit]
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
            if digit in node:
                count = node[digit]['count']
                win_amount = A[depth] if depth < len(A) else 0
                new_sum = current_sum + count * win_amount
                dfs(node[digit], depth + 1, new_sum)
            else:
                total = current_sum
                if total < min_total:
                    min_total = total
    
    dfs(prefix_tree, 0, 0)
    print(min_total)

if __name__ == "__main__":
    main()
