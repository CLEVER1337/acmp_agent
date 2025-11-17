package main
import . "fmt"
var (
	k, n int
	s    = ""
	d    [99][99][2][2]int
)

func F(i, z, t, q int) int {
	w := d[i][z][t][q]
	if i < n && w < 1 {
		x := 1
		if t > 0 {
			x = int(s[i] - 48)
		}
		y := 0
		for y <= x {
			o := 0
			if t > 0 && y == x {
				o = 1
			}
			if y > 0 {
				w += F(i+1, z, o, 1)
			} else if q == 1 {
				w += F(i+1, z+1-y, o, 1)
			} else {
				w += F(i+1, z, o, 0)
			}
			y++
		}
		d[i][z][t][q] = w
	} else if z == k {
		w = 1
	}
	return w
}

func main() {
	Scan(&n, &k)
	s = Sprintf("%b", n)
	n = len(s)
	Print(F(0, 0, 1, 0))
}