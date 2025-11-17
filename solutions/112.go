package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		n, k, t, h int
		e          [2e4]int
		r          = b.NewReader(Stdin)
	)

	Scan(&n, &k)
	for 0 < k {
		i := 0
		for i <= n {
			e[i] = 0
			i++
		}
		i = 0
		for i < n {
			Fscan(r, &h)
			j := n
			I := 0
			for I < 2 {
				u := 0
				for j > 0 {
					u += e[j]
					j -= j & -j
				}
				t += u * (1 - I*2)
				I++
				j = h
			}
			for h <= n {
				e[h]++
				h += h & -h
			}
			i++
		}
		k--
	}

	Print(t)
}