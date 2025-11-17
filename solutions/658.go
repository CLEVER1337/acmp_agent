package main
import . "fmt"
type B [4]uint

func T(s B, i int) bool { return s[i/64]&(1<<(i%64)) > 0 }
func (s B) A(o B) B     { return B{s[0] & o[0], s[1] & o[1], s[2] & o[2], s[3] & o[3]} }

func main() {
	var (
		p             [255]struct{ x, y int }
		w, h          [255][255]B
		r             B
		n, x, j, i, l int
	)

	Scan(&n)
	for j < n {
		Scan(&p[j].x, &p[j].y)
		j++
	}

	for i < n {
		j = i + 1
		for j < n {
			k := 0
			for k < n {
				if k != i && k != j {
					v := (p[j].x-p[i].x)*(p[k].y-p[i].y) - (p[j].y-p[i].y)*(p[k].x-p[i].x)
					if v < 0 {
						w[i][j][k/64] |= 1 << (k % 64)
					} else {
						h[i][j][k/64] |= 1 << (k % 64)
					}
				}
				k++
			}
			j++
		}
		i++
	}

	for l < n {
		j = l + 1
		for j < n {
			k := j + 1
			for k < n {
				e := w[l][j]
				if !T(e, k) {
					e = h[l][j]
				}
				z := w[l][k]
				if !T(z, j) {
					z = h[l][k]
				}
				t := w[j][k]
				if !T(t, l) {
					t = h[j][k]
				}
				if e.A(z).A(t) == r {
					x++
				}
				k++
			}
			j++
		}
		l++
	}

	Print(x)
}