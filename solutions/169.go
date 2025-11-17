package main
import . "fmt"
func main() {
	var (
		n, k, i int
		d       [90][90]int
	)

	Scan(&n, &k)

	m := n + k
	d[0][n] = 1
	for i < k {
		i++
		n = 1
		for n < m {
			a := d[i-1][n]
			d[i][n-1] += a
			n++
			if n <= m {
				d[i][n] += a
			}
		}
	}

	Print(d[k][0])
}