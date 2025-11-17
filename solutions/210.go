package main
import . "fmt"
type H struct {
	p, q []int
}
func N(x int) H {
	var (
		f H
		d = 2
		g = x
	)
	for x > 1 && d*d <= g {
		if x%d < 1 {
			f.p = append(f.p, d)
			f.q = append(f.q, 0)
		}
		for x%d < 1 {
			x /= d
			f.q[len(f.q)-1]++
		}
		d++
	}
	if x > 1 {
		f.p = append(f.p, x)
		f.q = append(f.q, 1)
	}
	return f
}

func main() {
	var (
		c H
		a = 0
		i = 0
		n = 1
	)

	Scan(&a)
	b := N(a)
	for i < len(b.p) {
		n *= b.p[i]
		i++
	}
	m := n
	for n <= a {
		w := N(n)
		c.p = w.p
		c.q = w.q
		i = 0
		j := 0
		for i < len(b.p) {
			for b.p[i] > c.p[j] {
				j++
			}
			if b.q[i] > c.q[j]*n {
				break
			}
			i++
		}
		if i == len(b.p) {
			break
		}
		n += m
	}

	Print(n)
}