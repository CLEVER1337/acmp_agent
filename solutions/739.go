package main
import . "fmt"
func main() {
	var (
		h    [123][]int
		x    [123]int
		k, i int
		s    = ""
	)

	Scan(&k, &s)
	n := len(s)
	for j, v := range s {
		h[v] = append(h[v], j)
	}

	w := make([]byte, n)
A:
	for i < n {
		j := byte(97)
		for j < 123 {
			if x[j] < len(h[j]) && h[j][x[j]]+k == i {
				x[j]++
				w[i] = j
				i++
				goto A
			}
			j++
		}
		j = 97
		for j < 123 {
			if x[j] < len(h[j]) {
				p := i - h[j][x[j]]
				if p < 0 {
					p = -p
				}
				if p <= k {
					w[i] = j
					x[j]++
					break
				}
			}
			j++
		}
		i++
	}

	Print(string(w))
}