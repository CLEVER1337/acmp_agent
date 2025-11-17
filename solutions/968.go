package main
import . "fmt"
func main() {
	var (
		z, v    [26]int
		a       = ""
		b       = a
		t, i, c int
	)

	Scan(&a, &b)
	n := len(a)
	for i < n {
		z[a[i]-97]++
		v[b[i]-97]++
		i++
	}

	for c < 26 {
		i = 0
		for i < 26 {
			q := c - i
			if q < 0 {
				q = -q
			}
			w := 26 - q
			if q < w {
				w = q
			}
			t += w * z[c] * v[i]
			i++
		}
		c++
	}

	Print(n * t)
}