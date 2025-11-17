package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		t          [202]int
		z, n, a, m int
		s          = b.NewReader(Stdin)
	)

	Scan(&n)
	for n > 0 {
		z++
		Fscan(s, &a)
		f := &t[a+101]
		b := z - *f
		if b > t[a] && *f > 0 {
			t[a] = b
		}
		*f = z
		n--
	}

	z = 1
	for z < 101 {
		if m < t[z] {
			m = t[z]
		}
		z++
	}

	Print(m)
}