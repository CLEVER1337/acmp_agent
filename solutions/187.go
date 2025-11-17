package main
import . "fmt"
func main() {
	var (
		m    [25][25]int
		n, j int
		i    = 1
	)

	Scan(&n)
	for j < n {
		m[0][j] = 1
		m[j][0] = 1
		j++
	}

	for i < 2*n-1 {
		j = i - n + 1
		if i < n {
			j = 1
		}
		for j < n+i && j < 2*n-1 {
			m[i][j] = m[i-1][j] + m[i-1][j-1] + m[i][j-1]
			j++
		}
		i++
	}

	Print(m[2*n-2][2*n-2])
}