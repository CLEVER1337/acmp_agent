package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)

type I = int
type T struct{ b, e, s I }

func M(a, b I) I {
	if a < b {
		b = a
	}
	return b
}

func main() {
	var (
		z                      []I
		n, c, e, a, x, y, j, i I
		r                      = b.NewReader(Stdin)
	)

	Scan(&n, &c, &e)
	q := make([]T, n)
	for j < n {
		Fscan(r, &a, &x, &y)
		if a < c {
			a = c
		}
		q[j] = T{a, M(x, e), y}
		j++
	}

	Slice(q, func(i, j I) bool {
		return q[i].e < q[j].e
	})

	j = 1
	for j < n {
		j *= 2
	}
	z = make([]I, 2*j)
	a = 3e9

	for i < n {
		h := 0
		if q[i].b != c {
			x = 0
			y = n
			for x < y {
				p := (x + y) / 2
				if q[p].e < q[i].b {
					x = p + 1
				} else {
					y = p
				}
			}
			y = i - 1 + j
			x += j
			h = 3e9
			for x <= y {
				if x&1 > 0 {
					h = M(h, z[x])
					x++
				}
				if y&1 < 1 {
					h = M(h, z[y])
					y--
				}
				x >>= 1
				y >>= 1
			}
		}
		x = i + j
		h += q[i].s
		z[x] = h
		for x > 1 {
			x >>= 1
			z[x] = M(z[x*2], z[x*2+1])
		}
		if q[i].e == e {
			a = M(a, h)
		}
		i++
	}

	if a > 2e9 {
		a = -1
	}

	Print(a)
}