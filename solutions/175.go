package main
import . "fmt"
type B byte
func main() {
	var (
		q       [4][7]B
		h, m, x int
		e       = []B{126, 48, 109, 121, 51, 91, 95, 112, 127, 123}
	)
	
	Scanf("%d:%d", &h, &m)
	for {
		i := 0
		k := 0
		o := []B{e[h/10], e[h%10], e[m/10], e[m%10]}

		if h/10 < 1 {
			o[0] = 0
		}

		for i < 4 {
			j := 0
			for j < 7 {
				if o[i]&(B(1)<<j) > 0 {
					q[i][j] |= 2
				} else {
					q[i][j] |= 1
				}
				j++
			}
			i++
		}

		for k < 4 {
			i = 0
			for i < 7 {
				if i > 3 && q[k][i] != 3 {
					goto A
				}
				i++
			}
			k++
		}
		Print(x)
		break
	A:
		m++
		if m > 59 {
			m = 0
			h++
			if h > 23 {
				h = 0
			}
		}

		x++
	}
}