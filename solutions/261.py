
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
    
    trie = {}
    for bet in bets:
        node = trie
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
                win = A[depth] * count
                new_sum = current_sum + win
                dfs(node[digit], depth + 1, new_sum)
            else:
                total = current_sum
                if total < min_total:
                    min_total = total
    
    dfs(trie, 0, 0)
    print(min_total)

if __name__ == "__main__":
    main()
