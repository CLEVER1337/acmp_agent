package main
import (
	. "fmt"
	. "sort"
)
func F(a string) string {
	A := []rune(a)
	Slice(A, func(i, j int) bool { return A[i] < A[j] })
	return string(A)
}
func main() {
	s := "YES"
	c := s
	d := s

	Scan(&c, &d)

	i := len(c)
	if F(c) != F(d) {
		s = "NO"
	}

	for 0 < i {
		i--
		if c[i] == d[i] {
			s = "NO"
		}
	}

	Print(s)
}