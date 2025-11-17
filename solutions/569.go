package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		q, z                   []int
		n, d, y, x, o, j, i, k int
		r                      = b.NewReader(Stdin)
	)

	Scan(&n, &d)
	e := make([]int, n)
	for j < n {
		Fscan(r, &o)
		e[j] = d - o
		j++
	}

	a := make([][2]int, n)
	for i < n {
		if e[i] > 0 {
			q = append(q, i)
		}
		i++
	}
	i = n
	for i > 0 {
		i--
		if e[i] < 0 {
			z = append(z, i)
		}
	}

	for y < len(q) && x < len(z) {
		j = q[y]
		i = z[x]
		a[j] = [2]int{i + 1, e[j]}
		e[i] += e[j]
		e[j] = 0
		y++
		if e[i] < 0 {
			z = append(z, i)
		}
		if e[i] > 0 {
			q = append(q, i)
		}
		x++
	}

	for k < n {
		j = a[k][1]
		Println(a[k][0], j)
		k++
	}
}