package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
func main() {
	var (
		s, i int
		h    [1e5][2]int
		r    = b.NewReader(Stdin)
	)

	Scan(&s, &i)
	for i > 0 {
		i--
		Fscan(r, &h[i][0], &h[i][1])
	}

	Slice(h[:], func(i, j int) bool {
		return h[i][1] > h[j][1]
	})

	for _, h := range h {
		if h[0] == s {
			s++
		} else if h[0]+1 == s {
			s--
		}
	}

	Print(s)
}