package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		N       = 500001
		p       [6e5]bool
		a       = ""
		c       = a
		l, h, o int
		j       = 2
		i       = 2
		r       = b.NewScanner(Stdin)
		P       = Print
	)

	r.Buffer([]byte{}, 1e6)
	r.Scan()
	s := r.Text()

	for j < N {
		p[j] = 1 > 0
		j++
	}

	for i*i < N {
		if p[i] {
			j = 2 * i
			for j < N {
				p[j] = 1 < 0
				j += i
			}
		}
		i++
	}

	N = len(s)
	q := N - 1
	j = 1
	for len(a)+len(c) < N {
		i = N - len(a) - len(c)
		if j > i {
			j = i
		}
		if h&1 > 0 {
			c = s[l:l+j] + c
			l += j
		} else {
			k := q - j + 1
			if k < l {
				k = l
			}
			a += s[k : k+j]
			q = k - 1
		}
		h++
		j++
	}

	s = a + c + "A"
	a = s[:1]
	for _, v := range s[1:] {
		if v > 64 && v < 91 {
			o++
			if p[o] {
				P(a)
			}
			a = ""
		}
		a += string(v)
	}
	if o < 2 {
		P("Impossible")
	}
}