package main
import . "fmt"
func main() {
	var n, m, i, f int

	Scan(&n, &m)
	t := n
	k := m
	for t*k > 0 {
		if t > k {
			t, k = k, t
		}
		k %= t
	}
	t += k
	for i < 2 {
		n /= t
		f++
		if n < 2 {
			f--
		}
		k = 2
		for k*k <= n {
			if n%k < 1 {
				f++
				n /= k
				k--
			}
			k++
		}
		n = m
		i++
	}

	Print(f)
}