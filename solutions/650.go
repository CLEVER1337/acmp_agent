package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
type I = int
var (
	q                [2e5][]I
	s, w             [2e5]I
	z, k, u, v, j, t I
	r                = b.NewReader(Stdin)
)

func F(E I) {
	v = j
	u = t - j - 1
	k += (v*(v-1) + u*(u-1)) / 2 * E
}

func main() {
	Scan(&z, &k)
	for 0 < k {
		Fscan(r, &u, &v)
		q[u] = append(q[u], v)
		q[v] = append(q[v], u)
		k--
	}

	for 0 < z {
		z--
		var (
			p    []I
			e, g I
		)
		j = 0
		t = 0
		s[t] = z
		t++
		w[z] = 1
		for t > 0 {
			u = s[t-1]
			t--
			p = append(p, u)
			for _, v := range q[u] {
				if w[v] < 1 {
					w[v] = 1
					s[t] = v
					t++
				}
			}
		}
		t = len(p)
		for _, v := range p {
			u = len(q[v])
			e += u & 1
			g += u / 2
		}
		if g == t-2 {
			for j < t {
				F(1)
				j++
			}
		}
		if g == t {
			j = t / 2
			F(t)
		}
	}

	Print(k)
}