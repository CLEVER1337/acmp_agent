package main
import . "fmt"
type M map[T]int
type T struct {
	a, b, c, d int
	e          *T
}
func main() {
	var (
		n, j, y, i, l int
		h             []int
		d             [1e3]T
		q             = []*T{{}}
		k             *T
		m             = M{}
		w             = M{}
		g             *T
		P             = Println
	)

	Scan(&n)
	for i < n {
		Scan(&j, &y)
		d[i] = T{j, y, 0, 0, k}
		m[d[i]] = i
		i++
	}

	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		if u.a == n-1 {
			g = u
			break
		}
		o := d[u.a]
		j = -1
		for j < 2 {
			i = -1
			for i < 2 {
				y = u.b + j
				c := u.c + i
				a, x := m[T{o.a + y, o.b + c, 0, 0, k}]
				if x {
					z := T{a, y, c, 0, k}
					if w[z] < 1 {
						w[z] = 1
						q = append(q, &T{a, y, c, u.d + 1, u})
					}
				}
				i++
			}
			j++
		}
	}

	n = -1
	if g != k {
		n = g.d
	}

	P(n)
	for g != k {
		h = append(h, g.a+1)
		g = g.e
	}

	n = len(h)
	for l < n {
		n--
		h[l], h[n] = h[n], h[l]
		l++
	}

	for _, v := range h {
		P(v)
	}
}