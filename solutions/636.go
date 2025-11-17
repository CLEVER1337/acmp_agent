package main
import . "fmt"
type I = int
type M struct{ a, b I }
var (
	d             [2][5e4 + 1]I
	z             [2e4]I
	p             [2e4][]I
	w             []M
	q             = []M{{}}
	h             M
	a, j, l, k, i I
)

func F(I I) {
	if d[I][j] < 0 {
		d[I][j] = d[h.a][h.b] + 1
		q = append(q, M{I, j})
	}
	l++
}

func main() {
	Scan(&a)
	for i < a {
		Scan(&j, &l)
		j--
		l--
		w = append(w, M{j, l})
		if l > z[j] {
			z[j] = l
		}
		d[1][i]--
		i++
		d[0][i]--
	}

	for i := range p {
		p[i] = make([]I, z[i]+1)
	}

	for i, w := range w {
		p[w.a][w.b] = i
	}

	for len(q) > 0 {
		h = q[0]
		q = q[1:]
		if h.a < 1 {
			l = -1
			for l < 2 {
				j = (h.b + l + a) % a
				F(0)
			}
		}
		i = w[h.b].a
		v := 1 + z[i]
		l = -1
		for l < 2 {
			y := w[h.b].b + l + v
			j = p[i][y%v]
			F(1)
		}
	}

	for k < a {
		j = d[0][k]
		i = d[1][k]
		if j < i {
			i = j
		}
		Println(i)
		k++
	}
}