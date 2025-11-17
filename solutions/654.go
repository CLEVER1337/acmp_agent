package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		k          []int
		n, m, v, t int
		s          = b.NewReader(Stdin)
	)

	Scan(&n, &m)
	l := m
	for 1 < n {
		Fscan(s, &t)
		if t > l {
			if t > m {
				m = t
			}
			q := len(k)
			for q > 1 {
				v += k[q-2] - k[q-1]
				l = k[q-2]
				k = k[:q-1]
				q = len(k)
			}

			v += t - l
			l = m
			if q > 0 {
				k = k[:q-1]
			}
		}

		if t < l {
			k = append(k, t)
			l = t
		}
		n--
	}

	Print(v + m - t)
}