package main
import . "fmt"
type T struct {
	u, v int
	d    float64
}
func main() {
	var (
		x, h       [101]float64
		q          []T
		s          = []int{1}
		n, e, u, k int
		i          = 1
		d          = 0.
		P          = Printf
	)

	Scan(&n, &e)
	for 0 < e {
		Scan(&u, &k, &d)
		if u > k {
			u, k = k, u
		}
		q = append(q, T{u, k, d})
		e--
	}

	h[1] = 1
	for len(s) > 0 {
		y := len(s) - 1
		u = s[y]
		s = s[:y]
		for _, v := range q {
			if v.u == u && h[v.v] < 1 {
				k = v.v
			} else if v.v == u && h[v.u] < 1 {
				k = v.u
			} else {
				goto A
			}
			d = v.d
			if u >= k {
				d = -d
			}
			x[k] = x[u] + d
			h[k] = 1
			s = append(s, k)
		A:
		}
	}

	for e < n-1 {
		e++
		if h[e] < 1 {
			goto B
		}
	}

	for _, v := range q {
		d = x[v.u] - x[v.v]
		if d < 0 {
			d = -d
		}
		d -= v.d
		if d < 0 {
			d = -d
		}
		if d >= 1e-6 {
			goto B
		}
	}

	P(`YES
`)
	for i < n {
		P("%.3f ", x[i+1]-x[i])
		i++
	}
	return
B:
	P("NO")
}