
import sys

def sqdist(p, q):
    """squared Euclidean distance between two points p and q"""
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + dy * dy

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    triangles = []          # (points, sorted_distances)
    shapes = set()

    for _ in range(n):
        pts = [(int(next(it)), int(next(it))) for __ in range(3)]
        d01 = sqdist(pts[0], pts[1])
        d12 = sqdist(pts[1], pts[2])
        d20 = sqdist(pts[2], pts[0])
        sorted_d = tuple(sorted([d01, d12, d20]))
        triangles.append((pts, sorted_d))
        shapes.add(sorted_d)

    # all triangles must have the same side lengths
    if len(shapes) != 1:
        print("NO")
        return

    # check handedness only for scalene triangles
    signs = set()
    for pts, sd in triangles:
        # sd[0] < sd[1] < sd[2]  <=>  scalene
        if sd[0] < sd[1] < sd[2]:
            # recompute the three distances
            d01 = sqdist(pts[0], pts[1])
            d12 = sqdist(pts[1], pts[2])
            d20 = sqdist(pts[2], pts[0])

            a, b, c = sd[0], sd[1], sd[2]

            # find the unique edge of length a
            if d01 == a:
                u, v, w = 0, 1, 2
            elif d12 == a:
                u, v, w = 1, 2, 0
            else:               # d20 == a
                u, v, w = 2, 0, 1

            # distances from w to u and v
            dwu = sqdist(pts[w], pts[u])
            dwv = sqdist(pts[w], pts[v])

            # i is the endpoint adjacent to a and b
            if dwu == b:
                i, j = u, v
            else:               # dwv == b
                i, j = v, u

            # cross product (k-i) × (j-i)
            dx_base = pts[j][0] - pts[i][0]
            dy_base = pts[j][1] - pts[i][1]
            dx_apex = pts[w][0] - pts[i][0]
            dy_apex = pts[w][1] - pts[i][1]

            cross = dx_apex * dy_base - dy_apex * dx_base
            if cross == 0:          # degenerate triangle – should not happen
                print("NO")
                return
            sign = 1 if cross > 0 else -1
            signs.add(sign)
            if len(signs) == 2:     # contradictory orientations already
                break

    # if all signs are equal (or there are no scalene triangles) -> YES
    print("YES" if len(signs) <= 1 else "NO")

if __name__ == "__main__":
    solve()
