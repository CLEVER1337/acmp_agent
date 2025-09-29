
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+n]
    m = int(data[1+n])
    patterns = data[2+n:2+n+m]
    
    trie = {}
    
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        if 'count' not in node:
            node['count'] = 0
        node['count'] += 1
    
    results = []
    for pattern in patterns:
        node = trie
        found = True
        for char in pattern:
            if char not in node:
                found = False
                break
            node = node[char]
        
        if not found:
            results.append('0')
        else:
            def count_words(node):
                total = node.get('count', 0)
                for key, child in node.items():
                    if key != 'count':
                        total += count_words(child)
                return total
            
            results.append(str(count_words(node)))
    
    sys.stdout.write('\n'.join(results))

if __name__ == '__main__':
    main()
