package main
import (
	. "container/heap"
	. "fmt"
)

type S struct{ a, b, c int }
type P []*S

func (p P) Len() int           { return len(p) }
func (p P) Less(i, j int) bool { return p[i].a < p[j].a }
func (p P) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p *P) Push(x any)        { *p = append(*p, x.(*S)) }
func (p *P) Pop() any {
	o := *p
	n := len(o) - 1
	e := o[n]
	*p = o[:n]
	return e
}

func main() {
	var (
		g, d    [50][50]int
		n, m, i int
		y       P
	)

	Scan(&n, &m)
	for i < n {
		j := 0
		for j < m {
			Scan(&g[i][j])
			d[i][j] = 1 << 20
			j++
		}
		i++
	}

	Push(&y, &S{g[0][0], 0, 0})
	for y.Len() > 0 {
		z := Pop(&y).(*S)
		i = 0
		for i < 4 {
			h := z.b + i%2 - i/3*2
			u := z.c + 1 - i + i/3*2
			if h >= 0 && u >= 0 {
				l := z.a + g[h][u]
				if l < d[h][u] {
					d[h][u] = l
					Push(&y, &S{l, h, u})
				}
			}
			i++
		}
	}

	Print(d[n-1][m-1])
}