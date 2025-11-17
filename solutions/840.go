package main
import (
	. "fmt"
	. "math"
)

type S struct {
	x, y, z, r float64
}

func main() {
	var (
		x, y, z, r float64
		d          = map[int]int{0: 1}
		N, i, f    int
	)

	Scan(&x, &y, &z, &r)
	h := []S{{x, y, z, r}}
	Scan(&N)

	for i < N {
		Scan(&x, &y, &z, &r)
		q := S{x, y, z, r}
		w := len(h)
		h = append(h, q)
		d[w] = 1
		j := 0
		for j < w {
			b := h[j]
			a := q.x - b.x
			u := q.y - b.y
			p := q.z - b.z
			if Sqrt(a*a+u*u+p*p) < q.r+b.r {
				delete(d, w)
				delete(d, j)
			}
			j++
		}
		i++
		if len(d) < 1 {
			f = 1
			break
		}
	}

	Print(i * f)
}