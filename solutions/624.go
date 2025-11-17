package main
import (
	b "bufio"
	. "fmt"
	. "os"
)

type T struct{ a, b, c I }
type I int32

var (
	i, j, c, u, e, t, n I
	a, q                [6e4][]I
	w, z                [1e6 + 1]I
	m                   = ""
	r                   = b.NewReader(Stdin)
	S                   = Fscan
)

func main() {
	S(r, &t)
	for 0 < t {
		S(r, &c, &n)
		var h []I
		i = 0
		for i < c {
			S(r, &u)
			a[i] = make([]I, u)
			q[i] = make([]I, u)
			h = append(h, i)
			for j := range q[i] {
				q[i][j] = 78
			}
			j = 0
			for j < u {
				S(r, &e)
				if e > 0 {
					w[e] = i
					z[e] = j
				}
				a[i][j] = e
				j++
			}
			i++
		}
		m = `YES
`
		for _, v := range h {
			i = 0
			for i < I(len(a[v])) {
				s := []T{{v, i, 0}}
				for len(s) > 0 {
					g := len(s) - 1
					d := s[g]
					s = s[:g]
					o := d.a
					k := d.b
					if d.c > 0 {
						q[o][k] = 86
					}
					if q[o][k] < 86 {
						if q[o][k] < 69 {
							m = `NO
`
							break
						}
						q[o][k] = 68
						s = append(s, T{o, k, 1})
						if k > 0 {
							s = append(s, T{o, k - 1, 0})
						}
						if a[o][k] < 0 {
							k = -a[o][k]
							s = append(s, T{w[k], z[k], 0})
						}
					}
				}
				i++
			}
		}
		Print(m)
		t--
	}
}