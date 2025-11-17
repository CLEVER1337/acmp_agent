package main
import . "fmt"
type T [8]int
func main() {
	var (
		z, i int
		d    [8]string
		q    [8]T
	)

	for i < 8 {
		Scan(&d[i])
		i++
	}

	for 0 < i {
		i--
		j := 0
		for j < 8 {
			if q[i][j] < 1 {
				z++
				w := []T{{i, j}}
				q[i][j] = 1
				for len(w) > 0 {
					c := len(w) - 1
					x := w[c][0]
					y := w[c][1]
					w = w[:c]
					k := 0
					for k < 4 {
						o := x + (1-k&1*2)*(1-k/2)
						p := y + k - k&1*k - k/2
						if o >= 0 && o < 8 && p >= 0 && p < 8 && q[o][p] < 1 && d[x][y] != d[o][p] {
							q[o][p] = 1
							w = append(w, T{o, p})
						}
						k++
					}
				}
			}
			j++
		}
	}

	Print(z)
}