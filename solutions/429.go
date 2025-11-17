package main
import . "fmt"
var (
	v, l    [2e3]int
	c       [2e3][]int
	N, p, z int
	i       = 1
	t       = ""
	S       = Scan
	P       = Print
)

func F(n, d int) int {
	if l[n] > 0 {
		return v[n]
	}
	r := -2
	if d&1 > 0 {
		r = 2
	}
	for _, v := range c[n] {
		x := F(v, d+1)
		if x > r == (d&1 < 1) {
			r = x
		}
	}
	return r
}

func main() {
	S(&N)
	for i < N {
		i++
		S(&t, &p)
		c[p] = append(c[p], i)
		if t == "L" {
			S(&z)
			c[p] = append(c[p], i)
			v[i] = z
			l[i] = 1
		}
	}

	a := F(1, 0)
	if a > 0 {
		P("+")
	}

	P(a)
}