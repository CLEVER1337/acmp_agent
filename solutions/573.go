package main
import (
	. "fmt"
	. "math"
	. "sort"
)
type I = int
var (
	a          [105]struct{ t, x, y float64 }
	q          [105][]I
	z, w       [105]I
	v          = 0.
	b          = v
	h          = v
	m          = v
	n, j, k, i I
)

func F(v I) I {
	if w[v] < 1 {
		w[v] = 1
		for _, V := range q[v] {
			if z[V] < 1 || F(z[V]) > 0 {
				z[V] = v
				return 1
			}
		}
	}
	return 0
}

func main() {
	Scan(&n, &v)
	for j < n {
		j++
		Scanf(`
%f:%f %f %f`, &h, &m, &a[j].x, &a[j].y)
		a[j].t = h*60 + m
	}

	Slice(a[1:n+1], func(i, j I) bool {
		return a[1+i].t < a[1+j].t
	})

	for i < n {
		j = i
		for j < n {
			j++
			if (a[j].t-a[i].t)/60*v >= Hypot(a[i].x-a[j].x, a[i].y-a[j].y) {
				q[i] = append(q[i], j)
			}
		}
		i++
	}

	for k < n {
		k++
		j = 0
		for j < n {
			j++
			w[j] = 0
		}
		F(k)
	}

	for 0 < n {
		if z[n] < 1 {
			b++
		}
		n--
	}

	Print(b)
}