package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	g := 0
	r := b.NewReader(Stdin)
	S := Fscan

	S(r, &g)
	for g > 0 {
		var (
			C, D, E             [2e4]int
			n, a, v, w, t, z, j int
			o                   = 9 << 50
			s                   = "Accepted"
		)
		S(r, &n)
		for j < n {
			S(r, &a, &v)
			C[a]++
			C[v]--
			D[a] += j
			D[v] -= j
			j++
		}

		for z < 1e4 {
			t += C[z]
			if t < o {
				o = t
			}
			w += D[z]
			if t == 1 {
				E[w] = 1
			}
			z++
		}

		for 0 < n {
			n--
			if E[n]*o != 1 {
				s = "Wrong Answer"
			}
		}
		Println(s)
		g--
	}
}