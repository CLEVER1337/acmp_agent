package main
import . "fmt"
type A [100]int
var (
	M             [100]A
	q             [100][]int
	d, w, e       A
	t, N, z, l, i int
)
func F(u, p int) {
	e[u] = 1
	d[u] = t
	w[u] = t
	t++

	for _, v := range q[u] {
		if e[v] < 1 {
			F(v, u)
			l = w[v]
			if l > d[u] {
				z--
			}
			if l < w[u] {
				w[u] = l
			}
		}
		if v != p && d[v] < w[u] {
			w[u] = d[v]
		}
	}
}

func main() {
	Scan(&N)
	for l < N {
		j := 0
		for j < N {
			Scan(&M[l][j])
			j++
		}
		l++
	}

	for i < N {
		l = i + 1
		for l < N {
			if M[i][l] > 0 {
				q[i] = append(q[i], l)
				q[l] = append(q[l], i)
				z++
			}
			l++
		}
		i++
	}

	for 0 < N {
		N--
		F(N, 0)
	}

	Print(z)
}