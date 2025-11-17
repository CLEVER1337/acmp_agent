package main
import . "fmt"
func main() {
	var (
		s             [53][53]int
		n, m, v, y, x int
		S             = Scan
	)

	S(&n, &m)
	for y < 53 {
		x = 0
		for x < 53 {
			o := 1
			if y <= n && x <= m && x*y > 0 {
				o = 0
			}
			s[y][x] = o
			x++
		}
		y++
	}

	S(&n)
	for n > 0 {
		S(&m, &y, &x)
		d, b, c, a := &s[y][x], &s[y][x+1], &s[y+1][x], &s[y+1][x+1]
		w := [][]*int{
			{a, b, c},
			{a, c, d},
			{a, b, d},
			{b, c, d}}[m-1]
		if *w[0]+*w[1]+*w[2] < 1 {
			*w[0] = 1
			*w[1] = 1
			*w[2] = 1
			v += 3
		}
		n--
	}

	Print(v)
}