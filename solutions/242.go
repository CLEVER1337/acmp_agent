package main
import . "fmt"
type T map[int]int

func F(a, b T) T {
	q := T{}
	for v := range a {
		if b[v] > 0 {
			q[v] = 1
		}
	}
	return q
}

func main() {
	var (
		a                   [200][200]int
		q, h, z, g          [200]T
		e                   = &q
		o                   = &h
		m                   T
		n, k, i, j, l, v, I int
		f                   = 2
		P                   = Println
	)

	Scan(&n, &k)
	for i < n {
		j = 0
		for j < n {
			Scan(&a[i][j])
			j++
		}
		i++
	}

	for I < 2 {
		l = 0
		for l < n {
			(*e)[l] = T{}
			(*o)[l] = T{}
			w := T{}
			i = 0
			for i < n {
				v = a[i][l]
				if I < 1 {
					v = a[l][i]
				}
				if w[v] > 0 {
					(*o)[l][v] = 1
				} else {
					w[v] = 1
					(*e)[l][v] = 1
				}
				i++
			}
			l++
		}
		e = &z
		o = &g
		I++
	}

	o = &h
	for I > 0 {
		m = (*o)[0]
		i = 1
		for i < 2 {
			m = F(m, (*o)[i])
			i++
		}
		i = 2
		for i < n {
			m = F(m, (*o)[i])
			i++
		}
		for j = range m {
			P(n, j)
			return
		}
		o = &g
		I--
	}

	for f > 0 {
		m = (*e)[0]
		i = 1
		for i < 2 {
			m = F(m, (*e)[i])
			i++
		}
		i = 2
		for i < n {
			m = F(m, (*e)[i])
			i++
		}
		for j = range m {
			l = 0
			i = 0
			for i < n {
				l += (*o)[i][j]
				i++
			}
			if l > 1 {
				P(n+1, j)
				return
			}
		}
		e = &q
		o = &h
		f--
	}

	m = T{}
	for f < n {
		x := F(m, h[f])
		if len(x) < 1 {
			m = h[f]
		} else {
			m = x
			l = 0
			for l < k {
				l++
				if F(m, q[f])[l] > 0 {
					P(n+2, l)
					return
				}
			}
		}
		f++
	}
}