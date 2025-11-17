package main
import . "fmt"
func main() {
	var (
		a             [100]int
		b, q, d, i, j int
		m             = map[int]int{}
		P             = Println
	)

	Scan(&b, &q)
	for i < q {
		Scan(&a[i])
		i++
	}

	q--
	for j < q {
		i = a[j] / (a[j] - a[j+1])
		if m[i] > 0 {
			m[i]--
		} else {
			P(i)
			d++
		}
		m[i-1]++
		j++
	}

	j = a[q]
	for v := range m {
		i = 0
		for i < m[v] {
			j /= v
			i++
		}
	}

	if j > 1 {
		P(j)
		d++
	}

	for d < b {
		P(1)
		d++
	}
}