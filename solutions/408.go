package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		e    [][]byte
		k, n int
		r    = b.NewReader(Stdin)
		P    = Println
	)

	Scanln(&k, &n)
	for 0 < n {
		q, _ := r.ReadBytes('\n')
		x := len(q) - 2
		q = q[:x]
		z := 0
		for q[z] == ' ' {
			z++
		}
		for q[x-1] == ' ' {
			x--
		}
		q = q[z:x]
		if len(q) > k {
			P("Impossible.")
			return
		}
		e = append(e, q)
		n--
	}

	for _, v := range e {
		h := make([]byte, k)
		for i := range h {
			h[i] = ' '
		}
		copy(h[(k-len(v))/2:], v)
		P(string(h))
	}
}