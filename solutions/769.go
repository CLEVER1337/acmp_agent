package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var (
		s             [1e4]string
		n, t, z, c, i int
	)

	Scan(&n)
	for i < n {
		Scan(&s[i])
		i++
	}

	Strings(s[:n])
	for z < n {
		i = len(s[t])
		for z < n && len(s[z]) >= i && s[z][:i] == s[t] {
			z++
		}
		t = z
		c++
	}

	Print(c)
}