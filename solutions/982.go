package main
import (
	. "fmt"
	. "sort"
)

type A [2]int
type B map[A]int

var (
	a    [8]string
	P    = Print
	I, j int
	g    = `
White: `
)

func D(r, c int, z B) B {
	e := byte(153 - g[1])
	d := 0
	for d < 4 {
		f := r + d&2 - 1
		m := c + d&1*2 - 1
		v := r + d&2*2 - 2
		k := c + d&1*4 - 2
		x := A{f, m}
		if v >= 0 && v < 8 && k >= 0 && k < 8 && a[f][m] == e && a[v][k] < 47 && z[x] < 1 {
			z[x] = 1
			for p := range D(v, k, z) {
				z[p] = 1
			}
		}
		d++
	}
	return z
}

func main() {
	for j < 8 {
		Scan(&a[j])
		j++
	}

	for I < 2 {
		var (
			b []A
			y = B{}
			i = 0
		)
		for i < 8 {
			j = 0
			for j < 8 {
				if a[i][j] == g[1] {
					for p := range D(i, j, B{}) {
						y[p] = 1
					}
				}
				j++
			}
			i++
		}
		i = len(y)
		P(g, i, `
`)
		for p := range y {
			b = append(b, p)
		}
		Slice(b, func(K, T int) bool {
			i = b[K][0]
			j = b[T][0]
			if i != j {
				return i < j
			}
			return b[K][1] < b[T][1]
		})
		for i, p := range b {
			P("(", p[0]+1, ", ", p[1]+1, ")")
			if i < len(b)-1 {
				P(", ")
			}
		}
		g = `
Black: `
		I++
	}
}