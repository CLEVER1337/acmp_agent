package main
import . "fmt"
type R struct{ x, y, a, b int }
type A [2]int
type T map[A]int
func main() {
	var (
		g                   [100]string
		m, n, k, c, x, y, i int
		d                   byte
		h                   = map[byte][]int{
			85: {0, -1}, 68: {0, 1},
			76: {-1, 0}, 82: {1, 0}}
		S = Scanln
	)

	S(&m, &n, &k)
	for i < n {
		S(&g[i])
		i++
	}

	o := make([]R, 0, k)
	for 0 < k {
		Scanf(`%d %d %c
`, &x, &y, &d)
		o = append(o, R{x - 1, y - 1, h[d][0], h[d][1]})
		k--
	}

	for len(o) > 0 {
		c++
		w := make([]R, 0, len(o))
		for _, r := range o {
			k = r.x + r.a
			i = r.y + r.b
			if k >= 0 && k < m && i >= 0 && i < n && g[i][k] < 88 {
				w = append(w, R{k, i, r.a, r.b})
			}
		}
		z := T{}
		for _, r := range w {
			z[A{r.x, r.y}]++
		}
		j := w[:0]
		for _, r := range w {
			if z[A{r.x, r.y}] == 1 {
				j = append(j, r)
			}
		}
		v := make([]R, 0, len(j))
		e := T{}
		for _, r := range j {
			k = r.x + r.a
			i = r.y + r.b
			for k >= 0 && k < m && i >= 0 && i < n && g[i][k] < 88 {
				e[A{k, i}] = 1
				k += r.a
				i += r.b
			}
		}
		for _, r := range j {
			if e[A{r.x, r.y}] < 1 {
				v = append(v, r)
			}
		}
		o = v
	}

	Print(c)
}