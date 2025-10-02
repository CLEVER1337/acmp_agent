
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    target1 = int(data[1])
    target2 = int(data[2])
    parents = [0] * (n + 1)
    
    for i in range(3, len(data)):
        parents[i - 2] = int(data[i])
    
    parents[1] = 0
    
    def get_path(start):
        path = []
        current = start
        while current != 0:
            path.append(current)
            current = parents[current]
        return path
    
    path1 = get_path(target1)
    path2 = get_path(target2)
    
    i = len(path1) - 1
    j = len(path2) - 1
    
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        i -= 1
        j -= 1
    
    lca = path1[i + 1]
    
    dist1 = len(path1) - (i + 2)
    dist2 = len(path2) - (j + 2)
    
    if dist1 <= dist2:
        print(target1)
    else:
        print(target2)

if __name__ == "__main__":
    main()
