package main
import (
	. "container/heap"
	. "fmt"
)

type I = int
type G struct{ v, x, i I }

type H []I
func (h H) Len() I           { return len(h) }
func (h H) Less(i, j I) bool { return h[i] > h[j] }
func (h H) Swap(i, j I)      { h[i], h[j] = h[j], h[i] }
func (h *H) Push(x any) { *h = append(*h, x.(I)) }
func (h *H) Pop() any {
	a := *h
	n := len(a) - 1
	x := a[n]
	*h = a[:n]
	return x
}

type E []G
func (h E) Len() I           { return len(h) }
func (h E) Less(i, j I) bool { return h[i].x > h[j].x }
func (h E) Swap(i, j I)      { h[i], h[j] = h[j], h[i] }
func (h *E) Push(x any) { *h = append(*h, x.(G)) }
func (h *E) Pop() any {
	a := *h
	n := len(a) - 1
	x := a[n]
	*h = a[:n]
	return x
}

func main() {
	var (
		q                                  [][]G
		g                                  [2e3][]G
		p                                  []G
		h                                  = &E{}
		a, b, c, d, r, x, i, l, j, y, k, m I
		z                                  = 1 << 31
	)

	Scan(&a, &b, &c)
	for l < b {
		l++
		Scan(&d, &r, &x)
		d--
		r--
		g[d] = append(g[d], G{r, x, l})
		g[r] = append(g[r], G{d, x, l})
	}

	if b == a {
		for i < a {
			if len(g[i]) != 1 {
				l = -1
				d = i
				for {
					q = append(q, []G{})
					r = -1
					for _, e := range g[d] {
						if e.v != l {
							if len(g[e.v]) == 1 {
								x = len(q) - 1
								q[x] = append(q[x], e)
							} else if r < 0 {
								r = e.v
								p = append(p, e)
							}
						}
					}
					l = d
					d = r
					if d == i {
						break
					}
				}
				break
			}
			i++
		}
		n := len(q)
		for j < n {
			X := &H{}
			r = 0
			for _, e := range q[j] {
				Push(X, e.x)
				r += e.x
			}

			l = j
			d = 0
			for {
				r += p[l].x
				l++
				l %= n
				d++
				if l == j {
					break
				}
				for _, e := range q[l] {
					Push(X, e.x)
					r += e.x
				}
				for X.Len() > c-d {
					r -= Pop(X).(I)
				}
				if X.Len() == c-d && r < z {
					z = r
					y = j
					k = l
					m = 0
				}
			}
			if d <= c {
				for X.Len() > c-d {
					r -= Pop(X).(I)
				}
				if X.Len() == c-d && r < z {
					z = r
					y = j
					k = j
					m = 1
				}
			}
			j++
		}
		if m > 0 {
			i = 0
			for i < n {
				for _, e := range q[i] {
					Push(h, e)
				}
				i++
			}
			for h.Len() > c-n {
				Pop(h)
			}
			i = 0
			for i < n {
				Push(h, p[i])
				i++
			}
		} else {
			i = y
			for {
				for _, e := range q[i] {
					Push(h, e)
				}
				if i == k {
					break
				}
				i++
				i %= n
				c--
			}
			for h.Len() > c {
				Pop(h)
			}
			i = y
			for i != k {
				Push(h, p[i])
				i++
				i %= n
			}
		}
	} else {
		for i < a {
			if len(g[i]) > 1 {
				o := 0
				for _, e := range g[i] {
					if len(g[e.v]) > 1 {
						o++
					}
				}
				if o == 1 {
					l = -1
					d = i
					for {
						q = append(q, []G{})
						r = -1
						for _, e := range g[d] {
							if e.v != l {
								if len(g[e.v]) == 1 {
									x = len(q) - 1
									q[x] = append(q[x], e)
								} else if r < 0 {
									r = e.v
									p = append(p, e)
								}
							}
						}
						l = d
						d = r
						if r < 0 {
							break
						}
					}
					break
				}
			}
			i++
		}
		n := len(q)
		for j < n {
			X := &H{}
			d = 0
			for _, e := range q[j] {
				Push(X, e.x)
				d += e.x
			}
			l = j + 1
			for l < n && l-j <= c {
				d += p[l-1].x
				for _, e := range q[l] {
					Push(X, e.x)
					d += e.x
				}
				for X.Len() > c-l+j {
					d -= Pop(X).(I)
				}
				if X.Len() == c-l+j && d < z {
					z = d
					y = j
					k = l
				}
				l++
			}
			j++
		}
		i = y
		for i <= k {
			for _, e := range q[i] {
				Push(h, e)
			}
			i++
		}
		for h.Len() > c-(k-y) {
			Pop(h)
		}
		i = y
		for i < k {
			Push(h, p[i])
			i++
		}
	}

	for _, V := range *h {
		Println(V.i)
	}
}