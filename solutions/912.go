package main
import . "fmt"
func main() {
	var (
		n, t, r, i int
		c          = 1
		a          [100]int
	)

	Scan(&n)
	for 0 < n {
		Scan(&t)
		a[t-1]++
		n--
	}

	for i < 99 {
		i++
		if a[i] == a[r] {
			c++
		}
		if a[i] > a[r] {
			r = i
			c = 1
		}
	}

	if c > 1 {
		r = -1
	}

	Print(r + 1)
}