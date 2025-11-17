package main
import . "fmt"
type I = int

var (
	w       []I
	a       [200]I
	q       [1e5][3]I
	n, j, i I
)

func F(p, h, o I) I {
	if q[p][h] < 2 {
		return q[p][h]
	}
	z := 0
	u := 1
	if p > 0 {
		u = 0
		l := 0
		for l < n {
			if (a[l]-a[o])%p == 0 {
				u++
			}
			l++
		}
	}
	if u&1 == 2-h && F(p, 3-h, o) < 1 {
		z = 1
		goto A
	}
	u = 0
	for u < n {
		x := a[u] - a[o]
		if x < 0 {
			x = -x
		}
		b := p
		for b > 0 {
			x, b = b, x%b
		}
		if x > 1 && (p < 1 || x < p) && F(x, 3-h, o) < 1 {
			z = 1
			goto A
		}
		u++
	}
A:
	q[p][h] = z
	return z
}

func main() {
	Scan(&n)
	for j < n {
		Scan(&a[j])
		j++
	}

	for i < n {
		j = 0
		for j < 1e5 {
			q[j][1] = 2
			q[j][2] = 2
			j++
		}
		if F(0, 2, i) < 1 {
			w = append(w, a[i])
		}
		i++
	}

	Println(len(w))
	for _, v := range w {
		Print(v, " ")
	}
}