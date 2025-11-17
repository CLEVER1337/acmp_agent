package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type A []int
func main() {
	var (
		d, y                [2e5]A
		p, x, z             [2e5]int
		n, k, t, l, i, e, f int
		q                   = A{1}
		o, h                A
		r                   = b.NewReader(Stdin)
		P                   = Println
		S                   = Fscan
	)
	z[1] = 1

	S(r, &n)
	for l < n {
		l++
		S(r, &p[l])
	}

	for i < n {
		i++
		S(r, &k)
		d[i] = make(A, k)
		l = 0
		for l < k {
			S(r, &d[i][l])
			l++
		}
	}

	for len(q) > 0 {
		i = len(q) - 1
		l = q[i]
		q = q[:i]
		for _, v := range d[l] {
			if z[v] < 1 {
				z[v] = 1
				q = append(q, v)
			}
		}
	}

	for e < n {
		e++
		if z[e] > 0 {
			for _, v := range d[e] {
				y[v] = append(y[v], e)
				x[e]++
			}
		}
	}

	for f < n {
		f++
		if z[f] > x[f] {
			h = append(h, f)
		}
	}

	for len(h) > 0 {
		i = len(h) - 1
		l = h[i]
		h = h[:i]
		o = append(o, l)
		t += p[l]
		for _, v := range y[l] {
			x[v]--
			if x[v] < 1 {
				h = append(h, v)
			}
		}
	}

	P(t, len(o))
	for _, v := range o {
		P(v)
	}
}