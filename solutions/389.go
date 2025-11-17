package main
import (
	b "bufio"
	. "fmt"
	. "os"
)

func F() {
	for _, v := range p {
		w := d[v]
		x := a[v] ^ a[(v+1)%n]
		h := x&(x-1) < 1
		d[v] = h
		if w && !h {
			q--
		}
		if !w && h {
			q++
		}
	}
}

var (
	d             [7e4]bool
	a             [7e4]int
	p             []int
	n, m, q, j, i int
	r             = b.NewReader(Stdin)
	S             = Fscan
)

func main() {
	S(r, &n)
	n = 1 << n
	for j < n {
		S(r, &a[j])
		j++
	}

	S(r, &m)
	for i < n {
		x := a[i] ^ a[(i+1)%n]
		if x&(x-1) < 1 {
			d[i] = 1 > 0
			q++
		}
		i++
	}

	for 0 < m {
		S(r, &i, &j)
		p = []int{i, j, (i - 1 + n) % n, (j - 1 + n) % n}
		F()
		a[i], a[j] = a[j], a[i]
		F()
		s := "No "
		if q == n {
			s = "Yes "
		}
		Print(s)
		m--
	}
}