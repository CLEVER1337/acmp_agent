package main
import (
	. "fmt"
	. "math/rand"
)
type T struct{ x, y int }
func main() {
	var (
		p []T
		P = Println
		n = 0
	)

	Scan(&n)
	for 0 < n {
		for {
			x := Intn(1e4)
			y := Intn(1e4)
			v := 1
			for _, i := range p {
				if i.x == x && i.y == y {
					v = 0
				}
			}
			j := 0
			for j < len(p) && v > 0 {
				k := j + 1
				for k < len(p) {
					a := p[j]
					b := p[k]
					c := T{x, y}
					if (b.x-a.x)*(c.y-a.y) == (b.y-a.y)*(c.x-a.x) {
						v = 0
					}
					k++
				}
				j++
			}
			if v > 0 {
				p = append(p, T{x, y})
				break
			}
		}
		n--
	}

	P("YES")
	for _, i := range p {
		P(i.x, i.y)
	}
}