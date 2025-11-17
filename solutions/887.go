package main
import (
	. "fmt"
	. "sort"
)

var (
	e                [2e4][]int
	d, y, h, o       [2e4]int
	n, x, l, k, g, m int
	P                = Println
)

func F(i int) int {
	if d[i] < 1 {
		p := e[i]
		Slice(p, func(i, j int) bool {
			return F(p[i]) < F(p[j])
		})
		t := 0
		z := 0
		for z < (len(p)+1)/2 {
			t += F(p[z])
			z++
		}
		d[i] = t + 1
	}
	return d[i]
}

func G(z int) {
	y[z] = 1
	w := e[z]
	i := 0
	for i < (len(w)+1)/2 {
		G(w[i])
		i++
	}
}

func H(i int) {
	h[i] = 1
	for _, v := range e[i] {
		if y[v] > 0 {
			H(v)
		}
	}
	o[g] = i
	g++
}

func main() {
	Scan(&n)
	for l < n {
		l++
		for {
			Scan(&x)
			if x < 1 {
				break
			}
			e[l] = append(e[l], x)
		}
	}

	F(1)
	G(1)
	for k < n {
		k++
		if y[k] > h[k] {
			H(k)
		}
	}

	P(g)
	for m < g {
		P(o[m])
		m++
	}
}