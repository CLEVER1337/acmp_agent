
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
        __slots__ = ('l', 'r', 'left', 'right', 'rev', 'sum')
        def __init__(self, l, r):
            self.l = l
            self.r = r
            self.left = None
            self.right = None
            self.rev = False
            self.sum = (l + r) * (r - l + 1) // 2
            
        def get_sum(self):
            if self.rev:
                return (self.l + self.r) * (self.r - self.l + 1) // 2 - self.sum
            return self.sum
            
        def update(self, l, r):
            if l > self.r or r < self.l:
                return
            if l <= self.l and self.r <= r:
                self.rev = not self.rev
                return
            mid = (self.l + self.r) // 2
            if self.left is None:
                self.left = Node(self.l, mid)
                self.right = Node(mid + 1, self.r)
            if self.rev:
                self.left.rev = not self.left.rev
                self.right.rev = not self.right.rev
                self.rev = False
            self.left.update(l, r)
            self.right.update(l, r)
            self.sum = self.left.get_sum() + self.right.get_sum()
            
        def query(self, l, r):
            if l > self.r or r < self.l:
                return 0
            if l <= self.l and self.r <= r:
                return self.get_sum()
            mid = (self.l + self.r) // 2
            if self.left is None:
                self.left = Node(self.l, mid)
                self.right = Node(mid + 1, self.r)
            if self.rev:
                self.left.rev = not self.left.rev
                self.right.rev = not self.right.rev
                self.rev = False
                self.sum = self.left.get_sum() + self.right.get_sum()
            res = self.left.query(l, r) + self.right.query(l, r)
            self.sum = self.left.get_sum() + self.right.get_sum()
            return res
    
    root = Node(1, N)
    output_lines = []
    
    for op in operations:
        op_type, L, R = op
        if op_type == 'I':
            root.update(L, R)
        else:
            s = root.query(L, R)
            output_lines.append(str(s))
            
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
