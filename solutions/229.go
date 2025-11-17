package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var (
		h, p          [1e3]float64
		q             []int
		s             = map[int]int{}
		n, i, l, I, o int
		w             = 1e-6
		P             = Println
	)

	Scan(&n)
	for i < n {
		Scan(&p[i], &h[i])
		i++
	}

	for I < 2 {
		for i, v := range p[:n] {
			z := 1.
			for j, V := range p {
				s := (h[j] - h[i]) / (v - V)
				if v > V+w && s > z {
					z = s
				}
			}
			for j, V := range p {
				if V*z > 100+w || v*z+h[i]+w < V*z+h[j] {
					goto A
				}
			}
			s[i+1] = 1
		A:
		}
		p, h = h, p
		I++
	}

	for k := range s {
		q = append(q, k)
		o++
	}
	Ints(q)

	P(o)
	for l < o {
		P(q[l])
		l++
	}
}