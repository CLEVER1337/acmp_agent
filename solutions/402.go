
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Point struct {
	x, y int
}

// gcd for int64 (coordinates are ≤ 10^4, safe in 64‑bit)
func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var N int
	if _, err := fmt.Fscan(in, &N); err != nil {
		return
	}
	pts := make([]Point, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}

	// remove duplicate points – they are indistinguishable for separating lines
	sort.Slice(pts, func(i, j int) bool {
		if pts[i].x == pts[j].x {
			return pts[i].y < pts[j].y
		}
		return pts[i].x < pts[j].x
	})
	uniq := make([]Point, 0, N)
	for _, p := range pts {
		if len(uniq) == 0 || p.x != uniq[len(uniq)-1].x || p.y != uniq[len(uniq)-1].y {
			uniq = append(uniq, p)
		}
	}
	pts = uniq
	N = len(pts)

	if N <= 1 {
		fmt.Println(0)
		return
	}

	// sum of distinct direction counts
	var sumK int64 = 0

	// for every point i compute number of distinct lines to earlier points
	for i := 0; i < N; i++ {
		dirMap := make(map[[2]int]struct{}) // key = (dx,dy)
		for j := 0; j < i; j++ {
			dx := pts[j].x - pts[i].x
			dy := pts[j].y - pts[i].y
			if dx == 0 && dy == 0 {
				continue // should not happen after deduplication
			}
			g := gcd(int64(dx), int64(dy))
			dx /= int(g)
			dy /= int(g)

			// canonical sign: first non‑zero component positive
			if dx < 0 || (dx == 0 && dy < 0) {
				dx = -dx
				dy = -dy
			}
			key := [2]int{dx, dy}
			dirMap[key] = struct{}{}
		}
		sumK += int64(len(dirMap))
	}

	// answer = 2 * sumK
	answer := 2 * sumK
	fmt.Println(answer)
}
