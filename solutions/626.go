package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type B = byte
func main() {
	var (
		h []B
		x = map[B]B{}
		i = 0
		s = b.NewScanner(Stdin)
	)
	s.Buffer(make([]B, 4096), 2e5)

	Scanln(&i)
	for 0 < i {
		s.Scan()
		z := s.Text()
		if len(z) == 2 {
			x[z[0]] = z[1]
		}
		i--
	}

	s.Scan()
	q := s.Text()
	for i < len(q) {
		v := len(h) - 1
		if v >= 0 {
			p := x[h[v]]
			if p == q[i] {
				h = h[:v]
				goto A
			}
		}
		h = append(h, q[i])
	A:
		i++
	}

	Print(string(h))
}