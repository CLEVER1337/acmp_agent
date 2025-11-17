package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type T struct{ a, b, c int }
func main() {
	var (
		s       [3e5]T
		n, x, i int
		r       = b.NewReader(Stdin)
	)

	Scan(&n)
	for i < n {
		Fscan(r, &s[i].a, &s[i].b)
		s[i].c = s[i].a + s[i].b
		i++
	}

	Slice(s[:n], func(i, j int) bool {
		return s[i].c > s[j].c
	})

	for 0 < n {
		n--
		if n&1 < 1 {
			x += s[n].a
		} else {
			x -= s[n].b
		}
	}

	Print(x)
}