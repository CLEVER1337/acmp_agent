
import sys
import math

EPS = 1e-9            # for strict inequalities
TWOPI = 2.0 * math.pi


def has_gap(theta, xs, ys, rs):
    """return True if for direction theta a bounded gap exists"""
    ct = math.cos(theta)
    st = math.sin(theta)
    L = [0.0] * len(xs)
    R = [0.0] * len(xs)
    for i in range(len(xs)):
        proj = xs[i] * ct + ys[i] * st
        L[i] = proj - rs[i]
        R[i] = proj + rs[i]

    order = sorted(range(len(xs)), key=lambda k: L[k])
    max_R = -1e100          # current maximal right end
    for pos, i in enumerate(order):
        if pos > 0 and L[i] > max_R + EPS:
            return True    # interior gap found
        if R[i] > max_R:
            max_R = R[i]
    return False


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    xs = []
    ys = []
    rs = []
    for _ in range(n):
        xs.append(float(next(it)))
        ys.append(float(next(it)))
        rs.append(float(next(it)))

    if n <= 1:                 # a single tree – forest is dense
        print("YES")
        return

    # ---- build candidate angles ---------------------------------
    angles = []
    for i in range(n):
        xi, yi, ri = xs[i], ys[i], rs[i]
        for j in range(i + 1, n):
            dx = xi - xs[j]
            dy = yi - ys[j]
            dist = math.hypot(dx, dy)               # > ri+rj
            sum_r = ri + rs[j]
            base = math.atan2(dy, dx)                # direction of Δ
            for s in (sum_r, -sum_r):
                if abs(s) > dist + EPS:              # should not happen
                    continue
                cos_phi = s / dist
                if cos_phi > 1.0:
                    cos_phi = 1.0
                if cos_phi < -1.0:
                    cos_phi = -1.0
                phi = math.acos(cos_phi)
                a1 = base + phi
                a2 = base - phi
                angles.append(a1 % TWOPI)
                angles.append(a2 % TWOPI)

    # safety – should never be empty, but keep it
    if not angles:
        angles = [0.0, math.pi / 2]

    angles.sort()
    uniq = []
    for a in angles:
        if not uniq or a - uniq[-1] > 1e-12:
            uniq.append(a)
    m = len(uniq)

    # ---- test every interval between consecutive candidate angles ----
    found = False
    for idx in range(m):
        a = uniq[idx]
        b = uniq[(idx + 1) % m] if idx + 1 < m else uniq[0] + TWOPI
        mid = (a + b) * 0.5
        if has_gap(mid, xs, ys, rs):
            found = True
            break

    # a few generic directions as a safety net
    if not found:
        for generic in (0.0, math.pi / 4, math.pi / 2, math.pi, 3 * math.pi / 2):
            if has_gap(generic, xs, ys, rs):
                found = True
                break

    print("NO" if found else "YES")


if __name__ == "__main__":
    solve()
