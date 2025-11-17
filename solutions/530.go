package main
import . "fmt"
func main() {
	var (
		n, m, i, j int
		s          = ""
		a          [200]string
		S          = Scan
		P = Print
	)

	S(&m, &n)
	for j < n*2 {
		S(&a[j])
		j++
	}

	S(&s)
	for i < n {
		j = 0
		for j < m {
			P(s[a[i][j]*2+a[n+i][j]-144] - 48)
			j++
		}
		P(`
`)
		i++
	}
}