package main
import . "fmt"
var (
	N    int = 1e6
	u, y [7e4]int
	m    [9][10][8]int
	x, l int
)

func g(p, q, w, z, c int) {
	if p == x {
		p = w<<8 | z
		if c < u[p] {
			u[p] = c
		}
		return
	}
	if q>>p&1 > 0 {
		g(p+1, q, w, z, c)
		return
	}

	for I, V := range []struct {
		a, b, c, d int
		t          bool
	}{
		{1, 1, 0, 0, 1 > 0},
		{2, 3, 0, 0, 1 > 0},
		{1, 1, 1, 0, w>>p&1 < 1},
		{3, 7, 0, 0, 1 > 0},
		{1, 1, 1, 1, w>>p&1 < 1 && z>>p&1 < 1},
		{2, 3, 1, 0, w>>p&1 < 1},
		{2, 3, 2, 0, w>>(p+1)&1 < 1},
		{1, 1, 3, 0, w>>p&3 < 1}} {
		if m[I+I/7][l][p] < N && q>>p&V.b < 1 && V.t {
			g(p+V.a, V.b<<p|q, V.c<<p|w, V.d<<p|z, c+m[I+I/7][l][p])
		}
	}

	if m[7][l][p] < N && q>>p&1 < 1 && p > 0 && w>>(p-1)&3 < 1 {
		g(p+1, 1<<p|q, 3<<(p-1)|w, z, c+m[7][l][p])
	}
}

func main() {
	var (
		e, k, p, z, i, j, o int
		r                   [10][8]int
		S                   = Scan
	)

	S(&e, &x, &k)
	for o < 9 {
		i = 0
		for i < 10 {
			j = 0
			for j < x {
				m[o][i][j] = N
				if o < 1 {
					r[i][j] = 2
					if i < e {
						S(&r[i][j])
					}
				}
				j++
			}
			i++
		}
		o++
	}

	for 0 < k {
		var c, a, b, d, i int
		S(&o, &c, &a)
		if o == 1 {
			for i < e {
				j = 0
				for j < x {
					if r[i][j] == a && c < m[0][i][j] {
						m[0][i][j] = c
					}
					j++
				}
				i++
			}
		}
		if o == 2 {
			S(&b)
			for i < e {
				j = 0
				for j+1 < x {
					v := r[i][j+1]
					f := r[i][j]
					if f == a && v == b ||
						f == b && v == a {
						if c < m[1][i][j] {
							m[1][i][j] = c
						}
					}
					j++
				}
				i++
			}
			i = 0
			for i+1 < e {
				j = 0
				for j < x {
					v := r[i+1][j]
					f := r[i][j]
					if f == a && v == b || f == b && v == a {
						if c < m[2][i][j] {
							m[2][i][j] = c
						}
					}
					j++
				}
				i++
			}
		}
		if o == 3 {
			S(&b, &d)
			for i < e {
				j = 0
				for j+2 < x {
					v := r[i][j+2]
					f := r[i][j+1]
					h := r[i][j]
					if h == a && f == b && v == d ||
						h == d && f == b && v == a {
						if c < m[3][i][j] {
							m[3][i][j] = c
						}
					}
					j++
				}
				i++
			}
			i = 0
			for i+2 < e {
				j = 0
				for j < x {
					v := r[i+2][j]
					f := r[i+1][j]
					h := r[i][j]
					if h == a && f == b && v == d ||
						h == d && f == b && v == a {
						if c < m[4][i][j] {
							m[4][i][j] = c
						}
					}
					j++
				}
				i++
			}
		}
		if o == 4 {
			S(&b, &d)
			for i+1 < e {
				j = 0
				for j+1 < x {
					v := r[i+1][j]
					f := r[i][j+1]
					h := r[i][j]
					V := r[i+1][j+1]
					if h == b && f == d && v == a {
						if c < m[5][i][j] {
							m[5][i][j] = c
						}
					}
					if h == a && f == b && V == d {
						if c < m[6][i][j] {
							m[6][i][j] = c
						}
					}
					if h == d && v == b && V == a {
						if c < m[8][i][j] {
							m[8][i][j] = c
						}
					}
					j++
					if f == a && V == b && v == d && c < m[7][i][j] {
						m[7][i][j] = c
					}
				}
				i++
			}
		}
		k--
	}

	for i := range u {
		y[i] = N
	}

	for k < x {
		if r[0][k] == 2 {
			p |= 1 << k
		}
		if r[1][k] == 2 {
			z |= 1 << k
		}
		k++
	}
	y[p<<8|z] = 0

	for l < e {
		for j := range u {
			u[j] = N
		}
		i = 0
		j = 0
		for j < x {
			if r[l+2][j] == 2 {
				i |= 1 << j
			}
			j++
		}
		j = 0
		for j < len(y) {
			if y[j] < N {
				g(0, j>>8, j&255, i, y[j])
			}
			j++
		}
		y, u = u, y
		l++
	}

	x = 1<<x - 1
	x = y[x<<8|x]
	if x >= N {
		x = -1
	}

	Print(x)
}