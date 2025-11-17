package main
import (
	. "fmt"
	. "sort"
)
func main() {
	s := ""
	Scan(&s)

	var (
		n = len(s)
		p = n
		q []int
		c = 0
		i = 1
	)

	for i*i <= n {
		if n%i < 1 {
			q = append(q, i, n/i)
		}
		i++
	}

	Ints(q)
	for _, v := range q {
		i = 0
		for i < n {
			if s[i] != s[i%v] {
				goto A
			}
			i++
		}
		p = v
		break
	A:
	}

	for 0 < n {
		c++
		n -= p
	}

	Print(c)
}