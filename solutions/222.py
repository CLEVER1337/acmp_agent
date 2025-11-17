
import sys
import math

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    ox = float(next(it))
    oy = float(next(it))

    TWO_PI = 2.0 * math.pi
    EPS = 1e-12

    intervals = []

    for _ in range(N):
        x = float(next(it))
        y = float(next(it))
        r = float(next(it))

        dx = x - ox
        dy = y - oy
        d = math.hypot(dx, dy)

        # observer inside or on a tree – according to the statement this never happens,
        # but we handle it for safety.
        if d <= r + EPS:
            print("YES")
            return

        # half angular width
        ratio = r / d
        if ratio > 1.0:
            ratio = 1.0
        alpha = math.asin(ratio)          # in (0, π/2)

        theta0 = math.atan2(dy, dx)
        if theta0 < 0.0:
            theta0 += TWO_PI

        # interval length
        length = 2.0 * alpha               # > 0, < π

        # bring start into [0, 2π)
        start = theta0 - alpha
        start_mod = start % TWO_PI

        # end position (may be > 2π)
        end = start_mod + length

        # a single interval longer than the whole circle is impossible,
        # but we keep the check for completeness.
        if length >= TWO_PI - EPS:
            print("YES")
            return

        if end <= TWO_PI:
            intervals.append((start_mod, end))
        else:
            # split across the 0 angle
            intervals.append((start_mod, TWO_PI))
            intervals.append((0.0, end - TWO_PI))

    if not intervals:
        print("NO")
        return

    intervals.sort()
    current_end = 0.0
    for l, r in intervals:
        if l > current_end + EPS:
            # a gap exists
            print("NO")
            return
        if r > current_end:
            current_end = r
            if current_end >= TWO_PI - EPS:
                print("YES")
                return

    # after processing all intervals
    if current_end >= TWO_PI - EPS:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
