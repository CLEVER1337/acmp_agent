package main
import . "fmt"
type T [100]int
func main() {
	var (
		d    [100]T
		a    T
		N, h int
	)

	Scan(&N)
	for h < N {
		Scan(&a[h])
		h++
	}

	h = 2
	for h < N {
		l := 0
		for l+h < N {
			r := l + h
			d[l][r] = 0
			if r-l > 1 {
				d[l][r] = 9e9
				k := l + 1
				for k < r {
					c := d[l][k] + d[k][r] + a[k]*(a[l]+a[r])
					if c < d[l][r] {
						d[l][r] = c
					}
					k++
				}
			}
			l++
		}
		h++
	}

	Print(d[0][N-1])
}