package main
import . "fmt"
func main() {
	var (
		p       [4e4]int
		n, m, a int
		o       = 1
		r       = 30000
	)

	Scan(&n, &m)
	for 0 < n {
		Scan(&a)
		p[a]++
		n--
	}

	for p[o] < 1 {
		o++
	}
	for p[r] < 1 {
		r--
	}

	for m > 0 {
		if m <= p[o] {
			n = o + 1
			if m < p[o] {
				n--
			}
			break
		}
		m -= p[o]
		p[o+1] += p[o]
		o++
		if o >= r {
			n = o + m/p[o]
			break
		}
	}

	Print(n)
}