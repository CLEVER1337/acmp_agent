package main
import (
	. "fmt"
	. "sort"
)
func main() {
	s := ""
	w := s

	Scan(&s, &w)
	S := len(s)
	W := len(w)
	l := S
	if W < l {
		l = W
	}

	for l > 0 {
		var (
			z          [3e3]int
			d, k, I, J int
			u          = 1
			m          = map[byte]int{
				65: 1,
				67: 1 << 16,
				71: 1 << 32,
				84: 1 << 48}
		)
		for J < 2 {
			i := 0
			for i < l {
				d += m[s[i]]
				i++
			}
			z[I] = d<<12 | J
			I++
			i = l
			for i < S {
				d += m[s[i]] - m[s[i-l]]
				i++
				z[I] = d<<12 | (i-l)*2 | J
				I++
			}
			s, w = w, s
			d, k = k, d
			S, W = W, S
			J++
		}
		Slice(z[:I], func(i, j int) bool {
			return z[i] < z[j]
		})
		for u < I {
			J = z[u] & 1
			if z[u]>>12 == z[u-1]>>12 && J != z[u-1]&1 {
				k = z[u] >> 1 & 2047
				d = z[u-1] >> 1 & 2047
				if J > 0 {
					k, d = d, k
				}
				Print(l, k+1, d+1)
				return
			}
			u++
		}
		l--
	}

	Print(0)
}