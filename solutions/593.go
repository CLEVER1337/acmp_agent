package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var n, j, i, l int

	Scan(&n)
	p := make([]struct{ x, y, i, a int }, n)
	for j < n {
		Scan(&p[j].x, &p[j].y)
		p[j].i = j
		j++
	}

	Slice(p, func(i, j int) bool {
		return p[i].x < p[j].x
	})

	for i < n {
		z := 0
		x := -1
		y := x
		j = i
		for j > 0 {
			j--
			w := p[i].x - p[j].x
			q := p[j].y - p[i].y
			if x < 0 || q*x >= y*w {
				z++
				x = w
				y = q
			}
		}
		x = -1
		y = x
		j = i + 1
		for j < n {
			w := p[j].x - p[i].x
			q := p[j].y - p[i].y
			if x < 0 || q*x >= y*w {
				z++
				x = w
				y = q
			}
			j++
		}
		p[i].a = z
		i++
	}

	Slice(p, func(i, j int) bool {
		return p[i].i < p[j].i
	})

	for l < n {
		Println(p[l].a)
		l++
	}
}