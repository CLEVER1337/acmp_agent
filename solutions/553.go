package main
import . "fmt"
type T [101]int
func main() {
	var (
		a    T
		d    [101]T
		n, i int
		l    = 2
	)

	Scan(&n)
	for i < n {
		Scan(&a[i], &a[i+1])
		i++
	}

	for l <= n {
		i = 0
		for i <= n-l {
			j := i + l
			d[i][j] = 1<<31 - 1
			k := i + 1
			for k < j {
				c := d[i][k] + d[k][j] + a[i]*a[j]
				if c < d[i][j] {
					d[i][j] = c
				}
				k++
			}
			i++
		}
		l++
	}
	Print(d[0][n])
}