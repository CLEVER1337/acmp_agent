package main
import . "fmt"
func main() {
	var (
		a          [21][21]int
		n, i, l, k int
		c          = 1
		s          = ""
		P          = Println
	)

	Scan(&n, &s)

	for l < n {
		l++
		j := 0
		for j < n {
			j++
			a[l][j] = c
			c++
		}
	}
	a[n][n] = 0
	x := n
	y := n
	for i < len(s) {
		p := &x
		j := 1
		f := &a[x-1][y]
		l = -1
		switch s[i] {
		case 82:
			p = &y
			j = n
			l = 1
			f = &a[x][y+1]
		case 76:
			p = &y
			f = &a[x][y-1]
		case 68:
			j = n
			l = 1
			f = &a[x+1][y]
		}
		i++
		if *p == j {
			P("ERROR", i)
			return
		}

		a[x][y], *f = *f, a[x][y]
		*p += l
	}

	for k < n {
		k++
		i = 0
		for i < n {
			i++
			P(a[k][i])
		}
	}
}