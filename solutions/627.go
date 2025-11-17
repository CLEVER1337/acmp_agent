package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		n, g, y, c, j, l int
		r                = b.NewReader(Stdin)
		e                = map[any]int{}
		x                = ""
		w                = x
		S                = Fscan
	)

	S(r, &x)
	for j < 2 {
		S(r, &n)
		i := 0
		for i < n {
			S(r, &w)
			t := map[any]int{}
			for _, v := range x {
				t[v]++
			}
			for _, v := range w {
				if t[v] < 1 {
					goto A
				}
				t[v]--
			}
			if j < 1 {
				e[w] = 1
				g++
			} else {
				if e[w] > 0 {
					c++
					g--
					y--
				}
				y++
			}
		A:
			i++
		}
		j++
	}

	for l < 3 {
		Println(F(g, y, c, l))
		l++
	}
}

func F(o, p, c, m int) int {
	for o+p+c > 0 {
		if o+c < 1 {
			return 2
		}
		if m == 1 {
			o--
		} else if c > 0 {
			c--
		} else {
			o--
		}
		if p < 1 {
			return 1
		}
		if m > 1 {
			p--
		} else if c > 0 {
			c--
		} else {
			p--
		}
	}
	return 0
}