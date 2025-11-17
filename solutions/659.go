package main
import (
	b "bufio"
	. "fmt"
	. "os"
)

var (
	n, u, h, a, c, g int
	q                [24][24]int
	w, z             [24]int
	r                = b.NewReader(Stdin)
)

func F(t, e, r int) {
	if t == n && r > g {
		g = r
		i := 0
		for i < n {
			z[i] = w[i]
			i++
		}
	}
	if e > 0 {
		w[t] = 1
		k := r
		i := 0
		for i < t {
			k += q[t][i] & w[i]
			i++
		}
		F(t+1, e-1, k)
	}
	if t+e < n {
		w[t] = 0
		k := r
		i := 0
		for i < t {
			k += q[t][i] & (1 - w[i])
			i++
		}
		F(t+1, e, k)
	}

}

func main() {
	Scan(&n, &u, &h)
	for 0 < h {
		Fscan(r, &a, &c)
		a--
		c--
		q[a][c] = 1
		q[c][a] = 1
		h--
	}

	F(0, u, 0)
	for 0 < n {
		n--
		if z[n] > 0 {
			Print(n+1, " ")
		}
	}
}