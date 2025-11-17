package main
import . "fmt"
func main() {
	var (
		d          = [1e5]int{1}
		A          [500]int
		n, t, c, i int
	)

	Scan(&n)
	for i < n {
		Scan(&A[i])
		t += A[i]
		i++
	}

	for _, a := range A {
		i = t
		for i >= a {
			if d[i-a] > 0 {
				d[i] = 1
			}
			i--
		}
	}

	for _, v := range d {
		c += v
	}

	Print(c)
}