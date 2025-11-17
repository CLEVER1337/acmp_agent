package main
import . "fmt"
func main() {
	n := 0
	m := 0
	Scan(&n, &m)

	a := n/m*m*(m-1)/2 + n%m*(n%m+1)/2
	k := n
	if k > m {
		a += (n - m) * m
		k = m
	}
	n = 1
	for n <= k {
		q := m / n
		r := m / q
		if r > k {
			r = k
		}
		c := r - n + 1
		a += c*m - q*(n+r)*c/2
		n = r + 1
	}

	Print(a)
}