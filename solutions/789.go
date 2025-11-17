package main
import . "fmt"
func main() {
	var (
		d          [1e4]int
		n, a, b, c int
		i          = 1
	)

	Scan(&n)
	d[0] = 1
	for i < n {
		z := d[a] * 2
		x := d[b] * 3
		y := d[c] * 5

		w := z
		if x < w {
			w = x
		}
		if y < w {
			w = y
		}

		d[i] = w
		if w == z {
			a++
		}
		if w == x {
			b++
		}
		if w == y {
			c++
		}
		i++
	}

	Print(d[n-1])
}