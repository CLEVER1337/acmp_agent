package main
import (
	. "fmt"
	. "sort"
)

func F(p []int, s int) int {
	i := SearchInts(p, s)
	if i < len(p) {
		return p[i]
	}
	return -1
}

func main() {
	var (
		e    []byte
		z, w [26][]int
		X    = ""
		Y    = X
		i, j int
	)

	Scan(&X, &Y)
	for i, c := range X {
		z[c-97] = append(z[c-97], i)
	}
	for i, c := range Y {
		w[c-97] = append(w[c-97], i)
	}

	for {
		u := 0
		c := 25
		for c >= 0 {
			a := F(z[c], i)
			b := F(w[c], j)
			if a != -1 && b != -1 {
				e = append(e, byte(97+c))
				i = a + 1
				j = b + 1
				u = 1
				break
			}
			c--
		}
		if u < 1 {
			break
		}
	}

	if len(e) > 0 {
		Print(string(e))
	}
}