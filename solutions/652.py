
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].split()
    N = int(first_line[0])
    K = int(first_line[1])
    
    operations = []
    for i in range(1, K + 1):
        parts = data[i].split()
        op_type = parts[0]
        L = int(parts[1])
        R = int(parts[2])
        operations.append((op_type, L, R))
    
    class Node:
        __slots__ = ['l', 'r', 'sum', 'rev', 'left', 'right']
        def __init__(self, l, r):
            self.l = l
            self.r = r
            self.sum = (l + r) * (r - l + 1) // 2
            self.rev = False
            self.left = None
            self.right = None
            
    root = Node(1, N)
    
    def push(node):
        if node.rev:
            node.rev = False
            mid = (node.l + node.r) // 2
            if node.left is None:
                node.left = Node(node.l, mid)
            if node.right is None:
                node.right = Node(mid + 1, node.r)
            node.left.rev = not node.left.rev
            node.right.rev = not node.right.rev
            left_sum = node.left.sum
            right_sum = node.right.sum
            node.left.sum = (node.l + mid) * (mid - node.l + 1) // 2 - left_sum
            node.right.sum = (mid + 1 + node.r) * (node.r - mid) // 2 - right_sum
            
    def update(node, l, r):
        if l > node.r or r < node.l:
            return
        if l <= node.l and node.r <= r:
            node.rev = not node.rev
            total = (node.l + node.r) * (node.r - node.l + 1) // 2
            node.sum = total - node.sum
            return
        push(node)
        mid = (node.l + node.r) // 2
        if node.left is None:
            node.left = Node(node.l, mid)
        if node.right is None:
            node.right = Node(mid + 1, node.r)
        if l <= mid:
            update(node.left, l, min(r, mid))
        if r > mid:
            update(node.right, max(l, mid + 1), r)
        node.sum = node.left.sum + node.right.sum
        
    def query(node, l, r):
        if l > node.r or r < node.l:
            return 0
        if l <= node.l and node.r <= r:
            return node.sum
        push(node)
        mid = (node.l + node.r) // 2
        res = 0
        if node.left and l <= mid:
            res += query(node.left, l, min(r, mid))
        if node.right and r > mid:
            res += query(node.right, max(l, mid + 1), r)
        return res
        
    output_lines = []
    for op in operations:
        op_type, L, R = op
        if op_type == 'I':
            update(root, L, R)
        else:
            s = query(root, L, R)
            output_lines.append(str(s))
            
    print('\n'.join(output_lines))

if __name__ == '__main__':
    main()
