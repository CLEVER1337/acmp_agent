package main
import . "fmt"
type I = int
var (
	n, k, x, y, l, h, i I
	N                   = 9 << 25
	q                   [155][]I
	d                   [155][155]I
)
func F(x, h I) I {
	t := 1
	d[x][1] = len(q[x])
	for _, v := range q[x] {
		if v != h {
			z := F(v, x)
			i := t + z
			for i > 0 {
				j := 0
				for j < i {
					j++
					w := d[x][i-j] + d[v][j] - 2
					if w < d[x][i] {
						d[x][i] = w
					}
				}
				i--
			}
			t += z
		}
	}
	return t
}

func main() {
	Scan(&n, &k)
	for i < n-1 {
		Scan(&x, &y)
		q[x] = append(q[x], y)
		q[y] = append(q[y], x)
		i++
	}

	for l < 155 {
		i = 0
		for i < 155 {
			d[l][i] = N
			i++
		}
		l++
	}

	F(1, -1)
	for h < n {
		h++
		if d[h][k] < N {
			N = d[h][k]
		}
	}

	Print(N)
}