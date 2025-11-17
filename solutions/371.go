package main
import . "fmt"
func main() {
	var (
		a       [1e6 + 2]int
		m, n, c int
		i       = 2
		j       = 2
		M       = 1000001
		P       = Println
	)

	for i < M {
		a[i] = 1
		i++
	}

	for j <= M/2 {
		i = j + j
		for i <= M {
			a[i] += j
			i += j
		}
		j++
	}

	Scan(&m, &n)

	i = m
	for i <= n {
		j = a[i]
		if j >= m && j <= n && a[j] == i && i < j {
			c++
			P(i, j)
		}
		i++
	}

	if c < 1 {
		P("Absent")
	}
}