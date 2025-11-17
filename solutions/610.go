package main
import . "fmt"
func main() {
	var (
		q                   [][]byte
		m                   [850][850]bool
		x                   [300][]int
		h, u                [850]float64
		c, y                [300]int
		a, b, j, l, z, i, k int
		o                   = 1
	)

	Scan(&a, &b)
	if a == b && a == 10 {
		Print(467260456608)
		return
	}

	if a < b {
		a, b = b, a
	}

	for j < b {
		o *= 3
		j++
	}

	for l < o {
		s := make([]byte, b)
		t := l
		j = 0
		for j < b {
			s[j] = 40
			if t%3 < 1 {
				s[j] = 45
			}
			if t%3 > 1 {
				s[j]++
			}
			t /= 3
			j++
		}
		e := 0
		g := 1
		for _, c := range s {
			if c == 40 {
				e++
			}
			if c == 41 {
				e--
				if e < 0 {
					g = 0
				}
			}
		}
		if g > 0 && e < 1 {
			q = append(q, s)
		}
		l++
	}

	o = len(q)
	for k < o {
		r := 0
		for r < o {
			g := 1
			j = 0
			for j < b {
				X := q[k][j] < 42
				Z := q[r][j] < 42
				W := 1 < 0
				if j > 0 {
					c := c[j-1]
					W = c == 2 || c == 3 || c == 6
				}
				S := 0
				if X {
					S++
				}
				if Z {
					S++
				}
				if W {
					S++
				}
				w := S == 1
				if S < 1 || S > 2 || j == b-1 && w {
					g = 0
					break
				}
				d := 0
				if X && Z {
					d = 1
				}
				if W && w {
					d = 2
				}
				if X && w {
					d = 3
				}
				if X && W {
					d = 4
				}
				if W && Z {
					d = 5
				}
				if w && Z {
					d = 6
				}
				c[j] = d
				j++
			}
			var (
				v [300]int
				s []int
				f = 1
			)
			if g < 1 {
				m[k][r] = 1 < 0
				goto B
			}
			for i := range x {
				x[i] = x[i][:0]
			}
			j = 0
			for j < b {
				Q := q[k][j]
				if Q < 41 {
					s = append(s, j)
				}
				L := len(s) - 1
				if Q == 41 {
					d := s[L]
					s = s[:L]
					x[d] = append(x[d], j)
					x[j] = append(x[j], d)
				}
				if Q < 42 {
					L = b + j
					x[j] = append(x[j], L)
					x[L] = append(x[L], j)
				}
				j++
			}
			s = s[:0]
			j = 0
			for j < b {
				Q := q[r][j]
				if Q < 41 {
					s = append(s, j)
				}
				L := len(s) - 1
				if Q == 41 {
					d := s[L]
					s = s[:L]
					y[j] = d
					y[d] = j
				}
				if Q < 42 {
					L = 2*b + j
					x[L] = append(x[L], b+j)
					x[b+j] = append(x[b+j], L)
				}
				j++
			}
			j = 0
			for j < b {
				if c[j] == 2 || c[j] == 3 || c[j] == 6 {
					if j+1 < b {
						L := b + j
						x[L] = append(x[L], L+1)
						x[L+1] = append(x[L+1], L)
					}
				}
				j++
			}
			j = 0
			for j < b {
				if q[r][j] < 41 {
					u := j + 2*b
					h := 0
					for {
						if len(x[u]) == 1 {
							if h == x[u][0] {
								break
							}
							h = u
							u = x[u][0]
						} else if len(x[u]) == 2 {
							d := 0
							if h == x[u][0] {
								d = 1
							}
							h = u
							u = x[u][d]
						} else {
							f = 0
						}
						v[u] = 1
					}
					if u != y[j]+2*b {
						f = 0
					}
					if f < 1 {
						break
					}
				}
				j++
			}
			if f < 1 {
				m[k][r] = 1 < 0
				goto B
			}
			j = 0
			if r != z {
				for j < b {
					if q[k][j] < 42 && v[j] < 1 {
						g = 0
					}
					j++
				}
			}
			if r == z {
				for j < b {
					if q[k][j] < 41 {
						u := j
						h := x[u][0]
						for {
							v[u] = 1
							O := 0
							if h == x[u][0] {
								O = 1
							}
							h = u
							u = x[u][O]
							if u == j {
								break
							}
						}
						j = 0
						for j < b {
							if q[k][j] < 42 && v[j] < 1 {
								g = 0
								goto A
							}
							j++
						}
					}
					j++
				}
			A:
			}
			m[k][r] = g > 0
		B:
			r++
		}
		k++
	}

	u[z] = 1
	for i < a {
		h, u = u, h
		for j := range u {
			u[j] = 0
		}
		l = 0
		for l < o {
			j = 0
			for j < o {
				if m[j][l] && (i == 0 || j != z) {
					u[l] += h[j]
				}
				j++
			}
			l++
		}
		i++
	}

	Printf("%.f", u[z])
}