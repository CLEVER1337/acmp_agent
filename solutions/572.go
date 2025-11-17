package main
import (
	. "container/heap"
	. "fmt"
	s "sort"
)

type F struct{ a, b, c int }
type H []F

func (h H) Len() int           { return len(h) }
func (h H) Less(i, j int) bool { return h[i].b < h[j].b }
func (h H) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *H) Push(x any)        { *h = append(*h, x.(F)) }
func (h *H) Pop() any {
	t := *h
	n := len(t) - 1
	x := t[n]
	*h = t[:n]
	return x
}

func main() {
	var (
		p, q, h       H
		w             []int
		n, c, a, b, i int
		P             = Println
		U             = Push
	)

	Scan(&n, &c)
	for i < n {
		i++
		Scan(&a, &b)
		f := F{a, b, i}
		if b < 0 {
			U(&q, f)
		} else {
			U(&p, f)
		}
	}

	s.Slice(p, func(i, j int) bool { return p[i].a < p[j].a })
	for _, f := range p {
		if c >= f.a {
			c += f.b
			w = append(w, f.c)
		}
	}

	s.Slice(q, func(i, j int) bool { return q[i].a+q[i].b > q[j].a+q[j].b })
	for _, f := range q {
		if c >= f.a {
			c += f.b
			U(&h, f)
			w = append(w, f.c)
		} else if len(h) > 0 {
			t := h[0]
			if t.b < f.b {
				Pop(&h)
				c += f.b - t.b
				U(&h, f)
				for i, v := range w {
					if v == t.c {
						w[i] = f.c
					}
				}
			}
		}
	}

	P(len(w))
	for _, v := range w {
		P(v)
	}
}