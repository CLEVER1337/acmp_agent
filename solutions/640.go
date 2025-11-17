package main
import . "fmt"
type S string
type R []S

var (
	x, y    R
	n, m, I int
	s       = "No"
)

func F(d R) R {
	n = len(d)
	m = len(d[0])
	r := make(R, m)
	I = 0
	for I < m {
		o := make([]byte, n)
		j := 0
		for j < n {
			o[j] = d[n-1-j][I]
			j++
		}
		r[I] = S(o)
		I++
	}
	return r
}

func P(d R) R {
	m = len(d)
	r := make(R, m)
	I = 0
	for I < m {
		s := []rune(d[I])
		j := 0
		n = len(s) - 1
		for j < n {
			s[j], s[n] = s[n], s[j]
			j++
			n--
		}
		r[I] = S(s)
		I++
	}
	return r
}

func main() {
	for I < 2 {
		var (
			s          [500]S
			f, b, i, j int
		)
		y = x
		Scan(&n, &m)
		for j < n {
			Scan(&s[j])
			j++
		}
		a := n
		c := m
		for i < n {
			j = 0
			for j < m {
				if s[i][j] < 36 {
					if i < a {
						a = i
					}
					if i > b {
						b = i
					}
					if j < c {
						c = j
					}
					if j > f {
						f = j
					}
				}
				j++
			}
			i++
		}
		if a > b {
			a = 0
			c = 0
		}
		x = make(R, b-a+1)
		i = a
		for i <= b {
			x[i-a] = s[i][c : f+1]
			i++
		}
		I++
	}

	for _, V := range []func(R) R{
		func(g R) R { return g },
		F,
		func(g R) R { return F(F(g)) },
		func(g R) R { return F(F(F(g))) },
		P,
		func(g R) R { return F(P(g)) },
		func(g R) R { return F(F(P(g))) },
		func(g R) R { return F(F(F(P(g)))) }} {
		r := V(y)
		n = 0
		for n < len(r) {
			if n >= len(x) || r[n] != x[n] {
				goto A
			}
			n++
		}
		s = "Yes"
	A:
	}

	Print(s)
}