
import sys
import heapq
from collections import defaultdict

INF = 10 ** 20


# -------------------------------------------------------------

def find(par, x):
    """iterative DSU find with path compression"""
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


# -------------------------------------------------------------
def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    pts = [(int(next(it)), int(next(it))) for _ in range(n)]

    # ---------- 1. vertical edges, first sweep (horizontal closing) ----------
    events_by_y = defaultdict(list)                     # y -> list of (x, delta)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if x1 == x2:                                   # vertical edge
            y_low = min(y1, y2)
            y_high = max(y1, y2)
            events_by_y[y_low].append((x1, +1))
            events_by_y[y_high].append((x1, -1))

    y_coords = sorted(events_by_y.keys())
    active_cnt = {}
    min_h = []          # min‑heap of x
    max_h = []          # max‑heap (store -x)
    slabs = []          # (y_start, y_end, L, R)

    for idx in range(len(y_coords) - 1):
        y = y_coords[idx]
        # process removals first, then additions
        for x, delta in events_by_y[y]:
            if delta == -1:
                active_cnt[x] = active_cnt.get(x, 0) - 1
                if active_cnt[x] == 0:
                    del active_cnt[x]
            else:
                active_cnt[x] = active_cnt.get(x, 0) + 1
                heapq.heappush(min_h, x)
                heapq.heappush(max_h, -x)

        # clean lazy deletions
        while min_h and min_h[0] not in active_cnt:
            heapq.heappop(min_h)
        while max_h and -max_h[0] not in active_cnt:
            heapq.heappop(max_h)

        if min_h:                               # interior exists
            L = min_h[0]
            R = -max_h[0]
            slabs.append((y, y_coords[idx + 1], L, R))

    # ---------- 2. compress x – column segments ----------
    xs_set = set()
    for y0, y1, L, R in slabs:
        xs_set.add(L)
        xs_set.add(R)
    xs = sorted(xs_set)                     # borders of column segments
    pos = {x: i for i, x in enumerate(xs)}
    K = len(xs) - 1                         # number of segments

    # ---------- 3. intervals for lowest / highest y per segment ----------
    intervals_low = []          # (y_start, seg_l, seg_r)
    intervals_high = []         # (y_end,   seg_l, seg_r)

    for y0, y1, L, R in slabs:
        l = pos[L]
        r = pos[R]              # exclusive
        if l < r:               # there is at least one column segment
            intervals_low.append((y0, l, r))
            intervals_high.append((y1, l, r))

    # ---- lowest y : scan intervals by increasing y_start ----
    min_y = [INF] * K
    parent = list(range(K + 1))               # DSU, parent[K] = K
    intervals_low.sort(key=lambda x: x[0])
    for y, l, r in intervals_low:
        i = find(parent, l)
        while i < r:
            min_y[i] = y
            parent[i] = i + 1
            i = find(parent, i)

    # ---- highest y : scan intervals by decreasing y_end ----
    max_y = [-INF] * K
    parent = list(range(K + 1))
    intervals_high.sort(key=lambda x: -x[0])
    for y, l, r in intervals_high:
        i = find(parent, l)
        while i < r:
            max_y[i] = y
            parent[i] = i + 1
            i = find(parent, i)

    # ---------- 4. second sweep (vertical closing) ----------
    events_final = []                     # (y, delta, segment idx)
    for i in range(K):
        if min_y[i] != INF:              # segment is covered
            events_final.append((min_y[i], +1, i))
            events_final.append((max_y[i], -1, i))

    events_final.sort(key=lambda x: x[0])

    # sweep over y
    y_vals = sorted({e[0] for e in events_final})
    active_seg_cnt = {}
    min_h = []
    max_h = []
    final_slabs = []                     # (y_start, y_end, L, R)

    p = 0
    m = len(events_final)
    for k in range(len(y_vals) - 1):
        y = y_vals[k]
        # process all events at this y
        while p < m and events_final[p][0] == y:
            _, delta, seg = events_final[p]
            if delta == +1:
                active_seg_cnt[seg] = active_seg_cnt.get(seg, 0) + 1
                heapq.heappush(min_h, seg)
                heapq.heappush(max_h, -seg)
            else:
                active_seg_cnt[seg] -= 1
            p += 1

        # clean heaps
        while min_h and active_seg_cnt.get(min_h[0], 0) == 0:
            heapq.heappop(min_h)
        while max_h and active_seg_cnt.get(-max_h[0], 0) == 0:
            heapq.heappop(max_h)

        if min_h:                       # there is a horizontal interval
            left_idx = min_h[0]
            right_idx = -max_h[0]
            L = xs[left_idx]
            R = xs[right_idx + 1]
            final_slabs.append((y, y_vals[k + 1], L, R))

    # ---------- 5. build polygon vertices ----------
    if not final_slabs:
        # degenerate – should not happen for a valid marsh area
        print(0)
        return

    Y = [final_slabs[0][0]]
    Llist = []
    Rlist = []
    for y0, y1, L, R in final_slabs:
        Y.append(y1)
        Llist.append(L)
        Rlist.append(R)
    M = len(Llist)                     # number of slabs

    verts = []
    # start (bottom‑left)
    verts.append((Llist[0], Y[0]))

    # bottom edge
    if Rlist[0] != Llist[0]:
        verts.append((Rlist[0], Y[0]))

    # right side upwards – add vertices only when the right border changes
    for i in range(M):
        if i < M - 1 and Rlist[i + 1] != Rlist[i]:
            verts.append((Rlist[i], Y[i + 1]))
            verts.append((Rlist[i + 1], Y[i + 1]))

    # ensure top‑right corner is present
    if verts[-1] != (Rlist[M - 1], Y[M]):
        verts.append((Rlist[M - 1], Y[M]))

    # top edge (horizontal step)
    if Llist[M - 1] != Rlist[M - 1]:
        verts.append((Llist[M - 1], Y[M]))

    # left side downwards – add vertices only when the left border changes
    for i in range(M - 1, -1, -1):
        if i > 0 and Llist[i - 1] != Llist[i]:
            verts.append((Llist[i], Y[i]))
            verts.append((Llist[i - 1], Y[i]))

    # the last edge (from last vertex back to first) is implicit

    # ---------- 6. output ----------
    out = [str(len(verts))]
    out += [f"{x} {y}" for x, y in verts]
    sys.stdout.write("\n".join(out))


# -------------------------------------------------------------
if __name__ == "__main__":
    solve()
