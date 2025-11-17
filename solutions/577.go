package main
import . "fmt"
func main() {
	var (
		n, m, k, i int
		d          [10]int
	)

	Scan(&n, &m)
	for i < n {
		i++
		j := 0
		for j < m {
			j++
			f := i * j
			for f > 0 {
				d[f%10]++
				f /= 10
			}
		}
	}

	for k < 10 {
		Println(d[k])
		k++
	}
}