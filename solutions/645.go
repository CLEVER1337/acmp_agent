package main
import . "fmt"
func main() {
	var k, h, w, i int

	Scan(&k)
	m := 2 * k
	for i < k {
		i++
		j := k / i
		l := i - j
		if l < 0 {
			l = -l
		}

		f := l + k - i*j
		if f < m {
			m = f
			h = i
			w = j
		}

	}

	Print(h, w)
}