package main
import . "fmt"
type T [5e3]int
func main() {
	var (
		a, b    T
		n, k, i int
		s       = ""
	)

	Scan(&n, &k, &s)
	c := n
	for i < n-1 {
		if s[i] != s[i+1] {
			b[i] = 1
		}
		if b[i] <= k {
			c++
		}
		i++
	}

	i = 1
	for i < n {
		i++
		var u T
		l := 0
		for l < n-i {
			u[l] = a[l+1]
			if s[l] != s[l+i] {
				u[l]++
			}
			if u[l] <= k {
				c++
			}
			l++
		}
		a = b
		b = u
	}

	Print(c)
}