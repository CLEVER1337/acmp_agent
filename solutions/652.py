
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    operations = []
    for i in range(1, 1 + k):
        parts = data[i].split()
        op_type = parts[0]
        l = int(parts[1])
        r = int(parts[2])
        operations.append((op_type, l, r))
    
    class Node:
        __slots__ = ('l', 'r', 'left', 'right', 'sum_val', 'rev')
        def __init__(self, l, r):
            self.l = l
            self.r = r
            self.left = None
            self.right = None
            self.sum_val = (l + r) * (r - l + 1) // 2
            self.rev = False
            
        def push(self):
            if self.rev:
                self.rev = False
                if self.left:
                    self.left.rev = not self.left.rev
                if self.right:
                    self.right.rev = not self.right.rev
                self.left, self.right = self.right, self.left
                
        def update(self, l, r):
            if l > self.r or r < self.l:
                return
            if l <= self.l and self.r <= r:
                self.rev = not self.rev
                return
            mid = (self.l + self.r) // 2
            if not self.left:
                self.left = Node(self.l, mid)
            if not self.right:
                self.right = Node(mid + 1, self.r)
            self.push()
            if l <= mid:
                self.left.update(l, min(r, mid))
            if r > mid:
                self.right.update(max(l, mid + 1), r)
            self.sum_val = self.left.get_sum() + self.right.get_sum()
            
        def get_sum(self):
            if self.rev:
                return (self.l + self.r) * (self.r - self.l + 1) // 2 - self.sum_val
            return self.sum_val
            
        def query(self, l, r):
            if l > self.r or r < self.l:
                return 0
            if l <= self.l and self.r <= r:
                return self.get_sum()
            self.push()
            res = 0
            mid = (self.l + self.r) // 2
            if l <= mid:
                res += self.left.query(l, min(r, mid))
            if r > mid:
                res += self.right.query(max(l, mid + 1), r)
            return res

    root = Node(1, n)
    output_lines = []
    
    for op in operations:
        op_type, l, r = op
        if op_type == 'I':
            root.update(l, r)
        else:
            s = root.query(l, r)
            output_lines.append(str(s))
            
    sys.stdout.write('\n'.join(output_lines))

if __name__ == '__main__':
    main()
