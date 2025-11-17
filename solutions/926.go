package main
import . "fmt"
func main() {
	var (
		n, k, i, l int
		a          [50]string
		P          = Print
	)

	Scan(&n)
	for i < n {
		Scan(&a[i])
		j := 0
		for j < n {
			if a[i][j] < 68 {
				k++
			}
			j++
		}
		i++
	}

	k /= 2
	for l < n {
		j := 0
		for j < n {
			i = 2
			if k > 0 {
				i = 1
			}

			P(i)
			if a[l][j] < 68 {
				k--
			}
			j++
		}
		P(`
`)
		l++
	}
}