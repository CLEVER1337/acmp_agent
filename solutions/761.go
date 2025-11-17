package main
import . "fmt"
type I int
var (
	w, x          [2e3]I
	q             [2e3][]I
	o             []I
	n, i, d, e, z I
)

func F(v I) {
	x[v] = 1
	o = append(o, v)
	for _, u := range q[v] {
		if x[u] < 1 {
			F(u)
		}
	}
}
func main() {
	Scan(&n, &i)
	for 0 < i {
		Scan(&d, &e)
		q[d] = append(q[d], e)
		q[e] = append(q[e], d)
		w[d]++
		w[e]++
		i--
	}

	for i < n {
		if x[i] < 1 {
			o = nil
			F(i)
			d = 0
			e = 0
			for _, v := range o {
				e += w[v]
				d += w[v] & 1
			}
			if e/2 > 0 {
				if d < 1 {
					d = 2
				}
				z += d / 2
			}
		}
		i++
	}

	Print(z)
}