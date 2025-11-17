package main
import . "fmt"

type T = string
type I = int
type M map[T]I

var (
	n, N, l I
	m       = 1
	w       [20]T
	u       = M{}
	p       = M{}
	P       = Println
	s       [10]T
	g       []T
)

func F(Q []T) []T {
	g = Q
	for _, x := range g {
		u[x] = 1
	}
	for _, x := range w[:N] {
		i := 0
		for i < n {
			i++
			p[x[:i]] = 1
		}
	}

	return s[:n*D(0)]
}

func D(r I) I {
	k := 0
	if r == n {
		for k < n {
			L := ""
			i := 0
			for i < n {
				L += T(s[i][k])
				i++
			}
			if u[L] < 1 {
				return 0
			}
			k++
		}
		return 1
	}
	for k < n {
		s[r] = g[k]
		j := 0
		for j < n {
			e := ""
			i := 0
			for i <= r {
				e += T(s[i][j])
				i++
			}
			if p[e] < 1 {
				goto A
			}
			j++
		}
		if D(r+1) > 0 {
			return 1
		}
	A:
		k++
	}
	return 0
}

func main() {
	Scan(&n)
	N = 2 * n
	for l < N {
		Scan(&w[l])
		l++
	}
	for m < 1<<N {
		x := m
		l = 0
		for x > 0 {
			l += x & 1
			x >>= 1
		}
		if l == n {
			var q, h []T
			l = 0
			for l < N {
				if m>>l&1 > 0 {
					q = append(q, w[l])
				} else {
					h = append(h, w[l])
				}
				l++
			}
			o := F(h)
			if len(o) > 0 {
				for _, r := range o {
					P(r)
				}
				P()
				for _, r := range F(q) {
					P(r)
				}
				return
			}
		}
		m++
	}
}