package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		n, m, x int
		r       = b.NewReader(Stdin)
		h       = map[int]int{}
		s       = ""
	)

	Scan(&n, &m, &x)
	for 0 < n {
		Fscan(r, &s)
		a := 0
		p := 1
		for _, v := range s {
			a += int(v-48) * p
			a %= m
			p *= x
			p %= m
		}
		h[a]++
		n--
	}

	for _, v := range h {
		n += v * (v - 1) / 2
	}

	Print(n)
}