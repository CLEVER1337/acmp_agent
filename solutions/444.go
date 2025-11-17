package main
import (
	. "fmt"
	. "sort"
)

func G(a int) string {
	s := ""
	w := s
	if a == 0 {
		s = "0"
	}
	if a < 0 {
		w = "-"
		a = -a
	}
	for a > 0 {
		s = Sprint(a%10) + s
		a /= 10
	}
	return w + s
}

func main() {
	var (
		x       []int
		n, t, i int
		P       = Print
		a       = map[int]int{}
		U       = ", "
	)

	Scan(&n)
	for 0 < n {
		Scan(&t)
		a[t] = 1
		n--
	}

	for s := range a {
		x = append(x, s)
	}

	Ints(x)
	n = len(x)
	for i < n-2 && n > 2 {
		if x[i]+1 == x[i+1] && x[i+1]+1 == x[i+2] {
			k := i + 1
			for k <= n-2 && x[k]+1 == x[k+1] {
				k++
			}
			w := G(x[i]) + ", ..., " + G(x[k])
			v := ""
			z := i
			for z <= k {
				v = v + G(x[z]) + U
				z++
			}
			v = v[:len(v)-2]
			if len(w) <= len(v) {
				v = w
			}
			P(v)
			i = k + 1
			if i < n {
				P(U)
			}
		} else {
			P(x[i], U)
			i++
		}
	}
	n--
	if i < n {
		P(x[i], U)
		i++
	}
	if i == n {
		P(x[i])
	}
}