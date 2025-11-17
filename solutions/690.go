package main
import . "fmt"
type T []int
func main() {
	var (
		q                [100]string
		f                []T
		D                = T{-2, -2, -1, -1, 1, 1, 2, 2, -1, 1, -2, 2, -2, 2, -1, 1}
		N, M, X, Y, i, j int
		P                = Print
	)

	Scan(&N, &M)
	for i < N {
		Scan(&q[i])
		j := 0
		for j < M {
			if q[i][j] > 46 {
				X = i
				Y = j
			}
			j++
		}
		i++
	}

	for j < 8 {
		a := X + D[j]
		i = Y + D[j+8]
		if a*i > 0 {
			f = append(f, T{a, i})
		}
		j++
	}

	for _, V := range f {
		var g []T
		u := 0
		for u < 8 {
			i = V[0] + D[u]
			j = V[1] + D[u+8]
			if i >= 0 && j > 0 {
				g = append(g, T{i, j})
			}
			u++
		}
		for _, U := range g {
			var (
				m, e [100][100]int
				p    = 3
				I    = 0
				h    = []T{{X, Y}, {V[0], V[1]}, {U[0], U[1]}}
			)
			for u, v := range h {
				e[v[0]][v[1]] = 1
				m[v[0]][v[1]] = u + 1
			}
			i = len(h) - 1
			x := h[i][0]
			y := h[i][1]
			for p < N*M {
				var (
					s, z, k int
					w       = 100
					r       []T
				)
				for k < 8 {
					i = x + D[k]
					l := y + D[k+8]
					if i >= 0 && i < N && l >= 0 && l < M && e[i][l] < 1 {
						o := 0
						j = 0
						for j < 8 {
							c := i + D[j]
							u = l + D[j+8]
							if c >= 0 && c < N && u >= 0 && u < M && e[c][u] < 1 {
								o++
							}
							j++
						}
						r = append(r, T{i, l, o})
					}
					k++
				}
				if len(r) < 1 {
					goto A
				}
				for _, d := range r {
					if d[2] < w {
						s = d[0]
						z = d[1]
						w = d[2]
					}
				}
				x = s
				y = z
				e[x][y] = 1
				p++
				m[x][y] = p
			}
			for I < N {
				j = 0
				for j < M {
					P(m[I][j], " ")
					j++
				}
				P(`
`)
				I++
			}
			return
		A:
		}
	}
}