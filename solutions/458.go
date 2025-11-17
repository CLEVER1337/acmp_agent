package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		g, o             [10]int
		w                [10]string
		e                = b.NewWriter(Stdout)
		r                = b.NewScanner(Stdin)
		H, t, j, i, l, f int
	)

	Scan(&H)
	for f < H {
		Scan(&l)
		g[f] = l
		f++
	}

	r.Scan()
	r.Scan()
	s := r.Text()

	n := len(s)
	W := (n + H - 1) / H
	for i < H {
		o[i] = W
		if i >= H-(W*H-n) {
			o[i]--
		}
		i++
	}

	for _, v := range g {
		if v > 0 && v <= H {
			v--
			i = t + o[v]
			w[v] = s[t:i]
			t = i
		}
	}

	for j < W {
		i = 0
		for i < H {
			if j < len(w[i]) {
				e.WriteByte(w[i][j])
			}
			i++
		}
		j++
	}
	e.Flush()
}