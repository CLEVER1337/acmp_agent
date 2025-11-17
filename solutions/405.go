package main
import . "fmt"
type I int
var (
	g             [2e4][]I
	h             [][]I
	t, w          [2e4]I
	a, i, d, m, q I
)

func F(v, p I) {
	t[v] = q
	w[v] = q
	q++
	z := 0
	for _, x := range g[v] {
		if t[x] < 0 {
			o := q
			F(x, v)
			z++
			if p > -1 && w[x] >= t[v] || p < 0 && z > 1 {
				h[v] = append(h[v], q-o)
			}
			if w[x] < w[v] {
				w[v] = w[x]
			}
		} else if t[x] < w[v] {
			w[v] = t[x]
		}
	}
}

func main() {
	Scan(&a, &i)
	for 0 < i {
		Scan(&d, &m)
		d--
		m--
		g[d] = append(g[d], m)
		g[m] = append(g[m], d)
		i--
	}

	h = make([][]I, a)
	for i := range t {
		t[i]--
		w[i]--
	}

	F(0, -1)

	for i < a {
		d = 0
		if len(h[i]) > 0 {
			m = 0
			for _, x := range h[i] {
				m += x
			}
			h[i] = append(h[i], a-1-m)
			for _, x := range h[i] {
				d += x * (a - 1 - x)
			}
		}
		Println(d/2 + a - 1)
		i++
	}
}