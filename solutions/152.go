package main
import . "fmt"

var (
	d          [101][]int
	c          [101]int
	N, M, a, b int
	s          = "Yes"
)

func F(v int) {
	c[v] = 2
	for _, u := range d[v] {
		if c[u] < 1 {
			F(u)
		}
		if c[u] > 1 {
			s = "No"
		}
	}
	c[v] = 1
}

func main() {
	Scan(&N, &M)
	for 0 < M {
		Scan(&a, &b)
		d[a] = append(d[a], b)
		M--
	}

	for 0 < N {
		N--
		F(N)
	}

	Print(s)
}