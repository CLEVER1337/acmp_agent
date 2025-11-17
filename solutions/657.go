package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		r             = b.NewReader(Stdin)
		t, n, w, q, h int
		R             = "ERROR"
		S             = Fscan
	)

	S(r, &t)
	for 0 < t {
		S(r, &n, &w)
		x := w * 2
		y := w * 2
		e := [1e5]int{1}
		i := 1
		s := ""
		for 1 < n {
			S(r, &q)
			e[i] = h
			i++
			q *= 2
			if 5*q > 15*w {
				e[i] = h
				q /= 2
				i++
			}
			if x > q {
				x = q
			}
			if y < q {
				y = q
			}
			h = 1 - h
			n--
		}
		if 9*y > 11*x || i&1 > 0 {
			s = R
			goto A
		}
		x = 0
		for x < i {
			if e[x] == e[x+1] {
				s = R
				goto A
			}
			s += Sprint(e[x])
			x += 2
		}

	A:
		Print(s, `
`)
		t--
	}
}