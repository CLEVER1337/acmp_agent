package main
import (
	. "fmt"
	. "strings"
)
func main() {
	s := "1"
	c := s
	a := 0
	i := 1

	Scan(&c)
	for a < 1 {
		s += Sprint(i)
		a = Index(s, c)
		i++
	}

	Print(a)
}