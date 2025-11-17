package main
import (
	. "fmt"
	. "sort"
)
type A [55]int
type B []int
func main() {
	var (
		o, g, d, q       [55]A
		D                = B{1, 0, -1, 0, 0, 1, 0, -1}
		w, h, i, j, l, b int
		e                B
	)

	Scan(&w, &h, &i)

	for 0 < i {
		i--
		j = 0
		for j < 4 {
			Scan(&q[i][j])
			j++
		}
	}

	X := B{0, w}
	Y := B{0, h}

	for _, v := range q {
		i = v[0]
		j = v[1]
		if i == v[2] && i > 0 && i < w {
			X = append(X, i)
		}
		if j == v[3] && j > 0 && j < h {
			Y = append(Y, j)
		}
	}

	for b < 2 {
		Y, X = X, Y
		Ints(Y)
		j = 0
		i = 1
		for i < len(Y) {
			if Y[i] != Y[j] {
				j++
				Y[j] = Y[i]
			}
			i++
		}
		Y = Y[:j+1]
		b++
	}

	w = len(X)
	h = len(Y)

	for _, v := range q {
		b = v[0]
		u := v[1]
		x := v[2]
		y := v[3]
		I := 0
		for I < 2 {
			if b == x {
				if u > y {
					u, y = y, u
				}
				i = 0
				for i < w {
					if X[i] == b {
						j = 0
						for j < h-1 {
							if Y[j] >= u && Y[j+1] <= y {
								o[i][j] = 1
							}
							j++
						}
					}
					i++
				}
			}
			b, x, w, X, Y, o, g, h, y, u = u, y, h, Y, X, g, o, w, x, b
			I++
		}
	}

	for l < w-1 {
		j = 0
		for j < h-1 {
			if d[l][j] < 1 {
				b = 0
				s := []A{{l, j}}
				d[l][j] = 1
				i = len(s)
				for i > 0 {
					i--
					x := s[i][0]
					y := s[i][1]
					s = s[:i]
					b += (X[x+1] - X[x]) * (Y[y+1] - Y[y])
					for I, v := range []bool{
						x < w-2 && d[x+1][y]+o[x+1][y] < 1,
						0 < x && d[x-1][y]+o[x][y] < 1,
						y < h-2 && d[x][y+1]+g[y+1][x] < 1,
						0 < y && d[x][y-1]+g[y][x] < 1} {
						if v {
							p := x + D[I*2]
							f := y + D[I*2+1]
							d[p][f] = 1
							s = append(s, A{p, f})
							i++
						}
					}
				}
				e = append(e, b)
			}
			j++
		}
		l++
	}

	Ints(e)
	i = len(e)

	for i > 0 {
		i--
		Println(e[i])
	}
}