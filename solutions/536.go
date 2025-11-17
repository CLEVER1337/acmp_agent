package main
import (
	. "fmt"
	. "strconv"
)
func main() {
	var (
		d       = [6e4]int{1}
		N, C, K int
		s       = ""
		o       = 1
		i       = 1
	)

	Scan(&N, &C, &K, &s)
	for 0 < K {
		o *= 10
		K--
	}

	for i <= N {
		l := 1
		for l <= i && l < 11 {
			K = i - l
			w := s[K:i]
			q, _ := Atoi(w)
			if l < 2 || w[0] > 48 && len(w) < 11 && q <= C {
				d[i] += d[K]
				d[i] %= o
			}
			l++
		}
		i++
	}

	Print(d[N] % o)
}