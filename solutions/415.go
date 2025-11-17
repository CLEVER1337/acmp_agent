package main
import (
	. "fmt"
	. "strings"
)
func main() {
	a := ""
	b := a
	l := 2
	L := ToLower

	Scan(&a, &b)

	m := a + b
	for l > 0 {
		q := L(a)
		i := 0
		for i <= len(a) {
			w := q[:i] + L(b)
			k := 0
			c := 0
			for c < 3 {
				j := Index(w[k:], q)
				if j > -1 {
					k += j
					e := []rune(w)
					if e[i] > 90 {
						e[i] -= 32
					}
					if e[k] > 90 {
						e[k] -= 32
					}
					s := string(e)
					r := len(s)
					t := len(m)
					if r < t || (r == t && s < m) {
						m = s
					}
					k++
				}
				c++
			}
			i++
		}
		l--
		a, b = b, a
	}

	Print(m)
}