package main
import . "fmt"
type S struct{ a, b int }
func main() {
	var (
		w, q          [101][101]S
		a, b, c, d, i int
	)

	Scan(&a, &b, &c, &d)
	for i <= a {
		j := 0
		for j <= b {
			k := 0
			for k <= c {
				var z S
				for I, v := range []int{i, j, k} {
					if v > 0 {
						m := q[j][k]
						if I == 1 {
							m = w[j-1][k]
						}
						if I > 1 {
							m = w[j][k-1]
						}
						y := m.b + 1 + I
						h := m.a
						if y >= d {
							h++
							y = 0
						}
						if h > z.a || h == z.a && y > z.b {
							z = S{h, y}
						}
					}
				}
				w[j][k] = z
				k++
			}
			j++
		}
		q = w
		i++
	}

	Print(w[b][c].a)
}