package main
import . "fmt"
var (
	u          [50]bool
	m          = map[int]int{}
	c, n, i, j int
)

func F(v, s int) {
	t := 15
	if v, e := m[v]
	e {
		t = v
	}
	if t == 15 {
		m[v] = s
	} else {
		s = t + s
		if s == 0 {
			delete(m, v)
		} else {
			m[v] = s
		}
	}
}

func main() {
	Scan(&n, &i)
	for 0 < i {
		Scan(&j)
		j--
		u[j] = !u[j]
		i--
	}

	for i < 50 {
		if u[i] {
			var z, w []int
			p := i + 1
			j = 0
			for l, v := range m {
				z = append(z, l)
				w = append(w, v)
				j++
			}
			for 0 < j {
				j--
				g := z[j]
				s := p
				for s > 0 {
					g, s = s, g%s
				}
				g = z[j] / g * p
				if g < n {
					F(g, -2*w[j])
				}
			}
			F(p, 1)
		}
		i++
	}

	for l, v := range m {
		c += n / l * v
	}

	Print(c)
}