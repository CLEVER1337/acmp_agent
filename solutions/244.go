package main
import . "fmt"
func main() {
	var (
		u          [5e4]int
		n, k, z, i int
		m          = -1
		P          = Print
	)

	Scan(&n, &k)
	for z < n {
		Scan(&u[z])
		z++
	}

	for i < k {
		r := 0
		o := 0
		p := -1
		w := p
		x := i
		for x < n {
			if u[x] < 1 {
				r++
				if r < 2 {
					p = x
				}
			} else {
				o++
				if o < 2 {
					w = x
				}
			}
			x += k
		}

		if r*o > 0 {
			if r*o > r+o || m >= 0 {
				P("FAIL")
				return
			}

			m = w
			if m > p {
				m = p
			}
			if r*o != 1 {
				m = p
				if o == 1 {
					m = w
				}
			}
		}
		i++
	}

	P("OK ", m+1)
}