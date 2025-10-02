
import sys

class TrieNode:
    __slots__ = ['children', 'count']
    def __init__(self):
        self.children = {}
        self.count = 0

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+n]
    m = int(data[1+n])
    patterns = data[2+n:2+n+m]
    
    root = TrieNode()
    
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    results = []
    for pattern in patterns:
        node = root
        found = True
        for char in pattern:
            if char not in node.children:
                found = False
                break
            node = node.children[char]
        
        if found:
            results.append(str(node.count))
        else:
            results.append("0")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
