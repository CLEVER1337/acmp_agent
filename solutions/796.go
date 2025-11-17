package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type R []rune
func main() {
	var (
		x, y int
		i    = 1
		q    []R
		w    R
		s    = b.NewScanner(Stdin)
		P    = Printf
	)

	Scan(&x, &y)
	for s.Scan() {
		for _, v := range s.Text() {
			w = append(w, v)
		}
		w = append(w, 10)
	}

	q = append(q, R{w[0]})
	for i < len(w) {
		v := len(q) - 1
		if w[i]+w[i-1] < 32 {
			q = append(q, R{})
		} else {
			q[v] = append(q[v], w[i])
		}
		i++
	}
	for _, v := range q {
		var o []string
		e := 1
		for _, c := range v {
			if c > 47 && c < 58 || c > 96 && c < 123 || c > 64 && c < 91 {
				if e > 0 {
					o = append(o, "")
					e = 0
				}
			} else {
				e = 1
			}
			if c > 32 {
				o[len(o)-1] += string(c)
			}
		}
		if len(o) > 0 {
			i = 0
			for i < y {
				P(" ")
				i++
			}
			P(o[0])
			u := y + len(o[0])
			i = 1
			for i < len(o) {
				f := len(o[i])
				g := " %s"
				if u+f < x {
					u += 1 + f
				} else {
					g = `
%s`
					u = f
				}
				P(g, o[i])
				i++
			}
			P(`
`)
		}
	}
}