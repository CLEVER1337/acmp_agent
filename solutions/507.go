package main
import . "fmt"
type T [4]int
type M = map[any]int
func main() {
	var (
		n, i, l, j, z int
		v             = M{}
		m             = M{}
		t, u          []T
		b             [4]T
		a             T
		P             = Println
		S             = Scan
	)

	S(&n)
	for l < n {
		S(&a[l])
		l++
	}
	for i < n {
		j = 0
		for j < n {
			S(&b[i][j])
			j++
		}
		i++
	}

	q := []T{a}
	for len(q) > 0 {
		s := q[0]
		q = q[1:]
		if v[s] < 1 {
			v[s] = 1
			i = 0
			for i < n {
				j = 0
				for j < n {
					if s[i] > 0 && (i != j && s[j] > 0 || i == j && s[i] > 1) && (b[i][j] > 0 || b[j][i] > 0) {
						z = 0
						for z < n {
							r := 0
							for r < n {
								if s[z] > 0 && (z != r || s[z] > 1) && (z == r || s[r] > 0) {
									h := s
									k := b[z][r]
									w := b[r][z]
									if k > w {
										h[r]--
									}
									if k < w {
										h[z]--
									}
									if k*w > 0 {
										h[r]--
										q = append(q, h)
										h = s
										h[z]--
									}
									q = append(q, h)
								}
								r++
							}
							z++
						}
						goto A
					}
					j++
				}
				i++
			}
			t = append(t, s)
		A:
		}
	}

	for _, s := range t {
		if m[s] < 1 {
			m[s] = 1
			u = append(u, s)
		}
	}
	i = 1
	z = len(u)
	for i < z {
		j = i
		for j > 0 {
			x := u[j]
			y := u[j-1]
			l = 0
			for l < 4 {
				if x[l] < y[l] {
					u[j], u[j-1] = u[j-1], u[j]
					break
				}
				if x[l] > y[l] {
					l = 4
				}
				l++
			}
			j--
		}
		i++
	}

	P(z)
	for _, s := range u {
		P(s[0])
		i = 1
		for i < n {
			P(s[i])
			i++
		}
	}
}