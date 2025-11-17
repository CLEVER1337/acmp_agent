package main

import . "fmt"

func P(n int) int {
	r := 1
	if n >= 0 {
		i := 0
		for i < n {
			r *= 2
			i++
		}
	}
	return r
}

func main() {
	var (
		t, c, i, p int
		s          = ""
	)

	Scan(&s)
	L := len(s)

	if L > 1 {
		t = P(L) - 2
	}

	for i < L {
		v := s[i]
		if 52 < v {
			c += P(L - i - 1)
		}
		if 55 < v {
			c += P(L - i - 1)
		}
		if v != 52 && v != 55 {
			p = 1
			break
		}
		i++
	}

	i = 1
	for _, c := range s {
		if c != 52 && c != 55 {
			i = 0
		}
	}

	if p < 1 && i > 0 {
		c++
	}

	Print(t+c)
}