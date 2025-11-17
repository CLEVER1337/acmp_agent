package main
import . "fmt"
func main() {
	var (
		n, a, w, q int
		i          = 1
		h          = map[int]int{}
		p          [4e4]int
	)

	Scan(&n, &a, &w)
	for i < n {
		i++
		Scan(&p[i])
	}

	for a > 0 {
		h[a] = 1
		a = p[a]
	}

	for w > 0 {
		if h[w] > 0 {
			q = w
			w = 0
		}
		w = p[w]
	}

	Print(q)
}