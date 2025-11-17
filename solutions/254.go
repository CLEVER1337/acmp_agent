package main
import . "fmt"
func main() {
	var (
		n, m, i, f, t int
		o, p          [5e3]int
		S             = Scan
	)

	S(&n)
	for t < n {
		S(&o[t])
		t++
	}

	S(&m)
	for f < 201 {
		p[f] = f
		f++
	}

	for 0 < m {
		S(&f, &t)
		p[f] = t
		m--
	}

	for i < n {
		Println(p[o[i]])
		i++
	}
}