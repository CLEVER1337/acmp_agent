package main
import . "fmt"
type N struct { o, t int }

var (
	u, d                      [3e3]int
	g                         [3e3][]N
	n, m, f, o, c, l, e, i, h int
)

func F(v int) {
	u[v] = 1
	for _, w := range g[v] {
		o := w.o
		if u[o] < 1 {
			F(o)
		}
	}
}

func main() {
	h = 1e9
	Scan(&n, &m)
	for i < m {
		i++
		Scan(&f, &o, &c)
		g[f] = append(g[f], N{o, c})
	}
	i = 1
	for i < n {
		i++
		d[i] = -h
	}

	for l < n {
		l++
		j := 0
		for j < n {
			j++
			for _, k := range g[j] {
				w := d[j] + k.t
				if d[j] > -h && d[k.o] < w {
					d[k.o] = w
				}
			}
		}
	}

	for e < n {
		e++
		for _, j := range g[e] {
			i = j.o
			if d[e] > -h && d[i] < d[e]+j.t && u[i] < 1 {
				F(i)
			}
		}
	}

	a := Sprint(d[n])
	if d[n] == -h {
		a = ":("
	}
	if u[n] == 1 {
		a = ":)"
	}

	Print(a)
}