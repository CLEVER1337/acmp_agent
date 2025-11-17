package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type T struct{ a, b int }
func main() {
	var (
		s                []T
		p                [5e3][]int
		h                [6e3]int
		z, x, i, c, j, u int
		r                = b.NewReader(Stdin)
	)

	Scan(&z, &x, &i)
	for 0 < i {
		Fscan(r, &j, &u)
		j--
		p[j] = append(p[j], u-1)
		i--
	}

	for 0 < z {
		z--
		j = 0
		for j < x {
			h[j]++
			j++
		}
		for _, j := range p[z] {
			h[j] = 0
		}
		s = nil
		j = 0
		for j <= x {
			u = len(s)
			for u > 0 && s[u-1].b > h[j] {
				u--
				t := s[u]
				s = s[:u]
				e := h[j]
				if u > 0 && s[u-1].b > e {
					e = s[u-1].b
				}
				i = j - t.a
				c += (t.b - e) * i * (i + 1) / 2
				s = append(s, T{t.a, h[j]})
			}
			s = append(s, T{j, h[j]})
			j++
		}
	}

	Print(c)
}