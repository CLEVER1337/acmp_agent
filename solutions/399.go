package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		a                [101][101]int
		s                [101]string
		n, m, p, v, i, u int
		r                = b.NewScanner(Stdin)
		x                = 2
		y                = 2
		o                = 1
	)

	Scan(&n, &m)

	for r.Scan() {
		s[i] = "@" + r.Text()
		i++
	}

	s[0] = s[0][1:]
	a[2][2] = 1

	for x != m-1 || y != n-1 {
		var d, f, k int
		z := 1 << 19

		for l, v := range [][2]int{
			{y + 1, x},
			{y, x + 1},
			{y - 1, x},
			{y, x - 1}} {
			q, g := v[0], v[1]
			if s[q][g] != 64 && a[q][g] < z {
				z = a[q][g]
				k = l
				d = g - x
				f = q - y
			}
		}

		if p > 1<<24 || z == 1<<19 {
			p = -1
			break
		}

		p++
		if k == u {
			x += d
			y += f
			a[y][x]++
		} else {
			if s[y+o][x+v] != 64 && a[y+f][x+d] == a[y+o][x+v] {
				x += v
				y += o
				k = u
				a[y][x]++
			} else {
				u = k
				x += d
				y += f
				a[y][x]++
				v = d
				o = f
			}
		}
	}

	Print(p)
}