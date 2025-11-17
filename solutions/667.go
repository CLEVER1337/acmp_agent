package main
import . "fmt"
func main() {
	var n, m, k, a int

	Scan(&n, &m, &k)
	if (n+m)%k > 0 {
		a = 1
	}
	a += (n + m) / k
	if m*(k-2) < n*2 {
		a = 0
	}

	Print(a)
}