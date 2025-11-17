package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		q, z, i int
		h       = 3
		p, o    [128]int
		r       = b.NewScanner(Stdin)
	)

	for i < 10 {
		for j, v := range r.Text() {
			if v > 31 {
				p[v] = j + 1
				o[v] = i
			}
		}
		i++
		r.Scan()
	}

	for _, v := range r.Text() {
		if v < 33 {
			z++
			q = 0
		}
		switch v {
		case 46, 63, 33:
			i = o[v]
			if i == q {
				z++
			}
			z += p[v]
			if h < 2 {
				h = 3
			}
			q = i
		}
		A := v < 91
		if v > 64 {
			if A {
				v += 32
			}
			i = o[v]
			if i == q {
				z++
			}
			z += p[v]
			if h > 1 && !A {
				z++
				h = 1
			}
			if A {
				if h < 2 {
					z++
					h = 2
				}
				if h > 2 {
					h = 1
				}
			}
			q = i
		}
	}

	Print(z)
}