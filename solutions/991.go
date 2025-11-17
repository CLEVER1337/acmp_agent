package main
import . "fmt"
type A [200]int
func main() {
	var (
		c, m       [100]A
		v, w, r, b A
		n, k, t, i int
	)

	Scan(&n, &k)
	for i < k {
		m[0][i] = 1
		i++
	}

	w[0] = k
	a := (n - 1) * k
	for a > 0 {
		for i := range v {
			v[i] = -1
		}
		q := v
		l := 0
		for l < n {
			u := 0
			i = 0
			for i < k {
				if m[l][i] < 1 && (v[l] < 0 || b[v[l]] > b[i]) {
					v[l] = i
				}
				i++
			}
			i = 0
			for v[l] >= 0 && i < n {
				if w[u] > w[i] && m[i][v[l]] > 0 {
					u = i
				}
				i++
			}
			if u >= 0 {
				o := q[u]
				p := c[u]
				if o < 0 || p[o] < p[l] || p[o] == p[l] && w[o] > w[l] {
					q[u] = l
				}
			}
			l++
		}
		t++
		i = 0
		for i < n {
			if q[i] > 0 {
				a--
				l = q[i]
				c[l][i]++
				w[l]++
				b[v[l]]++
				m[l][v[l]] = 1
				r[l] = t
			}
			i++
		}
	}

	i = 1
	for i < n {
		Println(r[i])
		i++
	}
}