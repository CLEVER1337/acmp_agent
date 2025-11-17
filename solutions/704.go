package main
import . "fmt"
func main() {
	var (
		c       [100][2]int
		N, M, i int
		o       = -200
		P       = Print
	)

	Scan(&N, &M)
	for i < M {
		Scan(&c[i][0], &c[i][1])
		i++
	}

	u := N
	for o < 201 {
		i = -200
		for i < 201 {
			if o != 0 || i != 0 {
				s := 0
				v := 1
				for _, p := range c[:M] {
					a := i*(2*p[0]-N) - o*(2*p[1]-u)
					if a == 0 {
						v = 0
						break
					}
					g := 1
					if a < 0 {
						g = -1
					}
					if s == 0 {
						s = g
					} else if s != g {
						v = 0
						break
					}
				}
				if v > 0 {
					P("YES")
					return
				}
			}
			i++
		}
		o++
	}
	P("NO")
}