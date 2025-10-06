
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    R = int(data[0])
    K = int(data[1])
    N = int(data[2])
    
    hairs = []
    index = 3
    for i in range(N):
        xh = float(data[index])
        yh = float(data[index+1])
        xs = float(data[index+2])
        ys = float(data[index+3])
        index += 4
        hairs.append((xh, yh, xs, ys))
    
    def get_angle(x, y):
        return (x, y)
    
    points = []
    for xh, yh, xs, ys in hairs:
        dx = xs - xh
        dy = ys - yh
        
        a = dx*dx + dy*dy
        b = 2*(xh*dx + yh*dy)
        c = xh*xh + yh*yh - R*R
        
        discriminant = b*b - 4*a*c
        t = (-b + discriminant**0.5) / (2*a)
        
        px = xh + t * dx
        py = yh + t * dy
        
        points.append((px, py))
    
    events = []
    for i, (px, py) in enumerate(points):
        angle = (px, py)
        events.append((angle, i))
    
    events.sort(key=lambda x: (x[0][0], x[0][1]))
    
    order = [0] * N
    for idx, (_, orig_idx) in enumerate(events):
        order[orig_idx] = idx
    
    class Fenw:
        def __init__(self, n):
            self.n = n
            self.tree = [0] * (n + 1)
        
        def update(self, index, delta):
            i = index + 1
            while i <= self.n:
                self.tree[i] += delta
                i += i & -i
        
        def query(self, index):
            res = 0
            i = index + 1
            while i > 0:
                res += self.tree[i]
                i -= i & -i
            return res
        
        def range_query(self, l, r):
            return self.query(r) - self.query(l - 1)
    
    fenw = Fenw(N)
    total = 0
    
    for i in range(N):
        pos = order[i]
        total += fenw.range_query(pos + 1, N - 1)
        fenw.update(pos, 1)
    
    print(total)

if __name__ == "__main__":
    main()
