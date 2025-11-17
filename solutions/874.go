package main
import . "fmt"
var (
	n, k, m, u, v int
	d             [8][8]int
	e             [8]int
)

func F(j int) {
	if j == n {
		m++
		return
	}
	c := 0
	for c < k {
		e[j] = c
		i := 0
		for i < j {
			if d[j][i] > 0 && e[i] == c {
				goto A
			}
			i++
		}
		F(j + 1)
	A:
		c++
	}
}

func main() {
	Scan(&n, &k, &m)
	for 0 < m {
		Scan(&u, &v)
		u--
		v--
		d[u][v] = 1
		d[v][u] = 1
		m--
	}
	F(0)

	Print(m)
}