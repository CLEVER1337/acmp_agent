package main
import . "fmt"
type T struct{ a, b int }
func main() {
	var (
		y, a, d                [2e4]int
		n, w, L, r, R, j, i, k int
		N                      = 1 << 30
		P                      = Print
	)

	Scan(&n, &w, &L, &r, &R)
	for j < L {
		Scan(&a[j])
		d[j] = N
		j++
	}
	q := L - w
	for i <= q {
		o := 0
		j = i
		for j < i+w {
			o += a[j]
			j++
		}
		y[i] = o
		if i >= r && i <= R {
			d[i] = o
		}
		i++
	}

	for 1 < n {
		n--
		var (
			b []T
			x [2e4]int
			l = 0
		)
		for l < L {
			x[l] = N
			l++
		}
		l = 0
		for l <= q {
			i = l - w - r
			if i > -1 {
				j = d[i]
				for len(b) > 0 && b[len(b)-1].b > j {
					b = b[:len(b)-1]
				}
				b = append(b, T{i, j})
			}
			for len(b) > 0 && b[0].a < l-w-R {
				b = b[1:]
			}
			if len(b) > 0 {
				x[l] = b[0].b + y[l]
			}
			l++
		}
		d = x
	}

	j = N
	for k <= q {
		i = L - k - w
		if i >= r && i <= R && d[k] < j {
			j = d[k]
		}
		k++
	}
	if j < N {
		P(j)
		return
	}
	P("No solution.")
}