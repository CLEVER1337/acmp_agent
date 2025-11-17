package main
import (
	. "fmt"
	. "math"
	. "math/big"
)
func main() {
	var (
		s = ""
		a = 0
		g = 1.
		h = 1e3
		w = map[any]int{"1": 0}
		N = NewInt
		L = Log10
		f = N(1)
		n = 1
	)

	for n < 101 {
		f.Mul(f, N(int64(n)))
		w[f.String()] = n
		n++
	}

	Scan(&s)
	c, o := w[s]
	if o {
		a = c
		goto A
	}

	c = len(s)
	for int(Log(6*h)/4+h*L(h/E)) < c {
		h *= 2
	}

	for g <= h {
		m := Floor((g + h) / 2)
		n := m
		if n < 1 {
			n = 1
		}
		e := int(Log(6*n)/4.4+n*L(n/E)) + 1
		if e < c {
			g = m + 1
		} else if e > c {
			h = m - 1
		} else {
			a = int(n)
			break
		}
	}
A:
	Print(a)
}