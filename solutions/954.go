package main
import . "fmt"
func main() {
	var (
		d          [7 << 14][7]int
		k, r, i, M int
		h          = 10
	)
	M = 1e6
	d[h][0] = 1
	d[h][3] = 1

	Scan(&k)
	for h < k {
		s := 0
		for s < 6 {
			t := d[h][s] % M
			if s != 2 {
				q := &d[h+1][s+1]
				*q = (*q + t) % M
			}
			if h < k-9 {
				q := &d[h+10][3-s/9]
				*q = (*q + t) % M
			}
			s++
		}
		h++
	}

	for i < 6 {
		r = (r + d[k][i]) % M
		i++
	}

	Print(r)
}