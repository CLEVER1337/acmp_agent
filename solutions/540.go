package main
import . "fmt"
func main() {
	var (
		a, b, c       [3e3]int
		n, m, d, j, l int
		i             = 1
	)

	Scan(&n, &m, &d)
	for j < m {
		Scan(&a[j])
		j++
	}
	for i < n {
		c = b
		b = a
		j = 0
		for j < m {
			h := 2
			k := 2
			if i < 3 {
				h = i
				k = 1
			}
			v := h * b[j+1]
			r := v
			if j > 0 {
				v = h * b[j-1]
				if j != m-1 {
					v += r - k*c[j]
				}
			}
			a[j] = (v + b[j]) % d
			if a[j] < 0 {
				a[j] += d
			}
			j++
		}
		i++
	}

	for l < m {
		Println(a[l])
		l++
	}
}