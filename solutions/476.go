package main
import . "fmt"
func main() {
	n := 0
	m := 0
	a := 1

	Scan(&m, &n)
	m--
	n--
	if m > n {
		m, n = n, m
	}

	if m == int(float64(n-m)*1.62) {
		a = 2
	}

	Print(a)
}