package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strings"
)
func main() {
	var (
		m, p [2e3]int
		r    = b.NewScanner(Stdin)
		x    = ""
		w    = x
		i, j int
		P    = Printf
	)

	r.Scan()
	q := ToLower(r.Text())
	for r.Scan() {
		x += r.Text() + `
`
	}

	for i, v := range x {
		if v < 33 {
			if i < 1 || x[i-1] > 32 {
				w += " "
				p[j] = i
				j++
			}
		} else {
			if v < 91 && v > 64 {
				v += 32
			}
			w += string(v)
			p[j] = i
			j++
		}
	}

	y := len(q)
	j = len(w) - y
	for i < j {
		if w[i:i+y] == q {
			m[p[i]] = 1
		}
		i++
	}

	for i, v := range x {
		if m[i] > 0 {
			P("@")
		}
		P("%c", v)
	}
}