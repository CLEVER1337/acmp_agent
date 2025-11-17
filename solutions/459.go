package main

import . "fmt"

var t = 1000

func F(x, y int, a [][]int) {
	for _, d := range [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}} {
		i, j := x+d[0], y+d[1]
		w := &a[i][j]
		if *w > a[x][y]+1 && *w != t {
			*w = a[x][y] + 1
			F(i, j, a)
		}
	}
}

func main() {
	var (
		n, e, s, w, o int
		f             = ""
		k             = f
	)

	Scan(&f)
	for _, h := range f {
		if h == 78 {
			n++
		}
		if h < 70 {
			e++
		}
		if h == 83 {
			s++
		}
		if h > 86 {
			w++
		}
	}

	a := make([][]int, 406)
	for i := range a {
		a[i] = make([]int, 406)
		for j := range a[i] {
			a[i][j] = t
		}
	}

	n = n*2 + 3
	w = w*2 + 3
	x, y := n, w
	a[x][y] = 0

	for _, h := range f {
		var z, v, j int

		if h == 78 {
			z = -1
		}
		if h < 70 {
			v = 1
		}
		if h == 83 {
			z = 1
		}
		if h > 86 {
			v = -1
		}

		for j < 2 {
			x += z
			y += v
			o++
			if a[x][y] == t {
				a[x][y] = o
			}
			j++
		}
	}

	F(n, w, a)

	for a[x][y] > 0 {
		w = 78
		o = a[x][y]

		for _, d := range []struct{ i, j, r int }{
			{-2, 0, w},
			{0, 2, 69},
			{2, 0, 83},
			{0, -2, 87}} {
			n, m := x+d.i, y+d.j
			if o > a[n][m] && a[x+d.i/2][y+d.j/2] != t {
				w = d.r
				o = a[n][m]
			}
		}

		k += string(w)
		if w == 78 {
			x -= 2
		}
		if w < 70 {
			y += 2
		}
		if w == 83 {
			x += 2
		}
		if w > 86 {
			y -= 2
		}
	}

	Print(k)
}
