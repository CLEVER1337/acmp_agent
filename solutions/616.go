package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		q, w, h, o    [1e3]int
		p             [1e3]string
		n, j, l, u, k int
		r             = b.NewReader(Stdin)
		P             = Print
	)

	Scan(&n)
	for j < n {
		Fscan(r, &p[j])
		h[j]--
		o[j]--
		i := 0
		for i < n {
			if p[j][i] > 48 {
				q[j]++
			} else {
				w[i]++
			}
			i++
		}
		j++
	}

	x := n
	y := n
	for k < 2*n {
		f := 0
		i := 0
		for i < n && f < 1 {
			if h[i] < 0 && q[i] == y {
				f = 1
				h[i] = k
				x--
				j = 0
				for j < n {
					if p[i][j] < 49 {
						w[j]--
					}
					j++
				}
			}
			i++
		}
		if f < 1 {
			i = 0
			for i < n && f < 1 {
				if o[i] < 0 && w[i] == x {
					f = 1
					o[i] = k
					y--
					j = 0
					for j < n {
						if p[j][i] > 48 {
							q[j]--
						}
						j++
					}
				}
				i++
			}
			if f < 1 {
				P("NO")
				return
			}
		}
		k++
	}

	P(`YES
`)
	for l < n {
		P(h[l], " ")
		l++
	}
	P(`
`)
	for u < n {
		P(o[u], " ")
		u++
	}
}