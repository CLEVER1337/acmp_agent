package main
import . "fmt"
func main() {
	var (
		o          [500][2]int
		d, g       [1e4]int
		e, F, N, l int
		q          = 1 << 30
		P          = Println
	)

	Scan(&e, &F, &N)
	F -= e
	for l < N {
		Scan(&o[l][0], &o[l][1])
		l++
	}

	l = 1
	for l <= F {
		d[l] = q
		l++
	}

	l = 1
	for l <= F {
		g[l]--
		l++
	}

	for _, u := range o {
		l = u[0]
		N = u[1]
		e = N
		for e <= F {
			if d[e-N] < q {
				v := d[e-N] + l
				if d[e] > v {
					d[e] = v
				}
			}
			if g[e-N] > -1 {
				v := g[e-N] + l
				if g[e] < v {
					g[e] = v
				}
			}
			e++
		}
	}

	if d[F] == q || g[F] < 0 {
		P("This is impossible.")
	} else {
		P(d[F], g[F])
	}
}