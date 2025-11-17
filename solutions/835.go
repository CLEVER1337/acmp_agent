package main
import . "fmt"
func main() {
	var (
		w, p                   [20]int
		s                      []int
		n, W, a, b, c, l, d, i int
		P                      = Println
	)

	Scan(&n, &W)
	for l < n {
		Scan(&w[l], &p[l])
		l++
	}

	for d < 1<<n {
		var e, f, g, l, k int
		for l < n {
			if d>>l&1 > 0 {
				e += w[l]
				f += p[l]
				g++
			}
			l++
		}
		y := 1 > 0
		for k < n {
			o := d>>k&1
			p := b>>k&1
			if o != p {
				y = o > p
				break
			}
			k++
		}
		if e <= W && (f > c || f == c && (g < a || g == a && y)) {
			c, a, b = f, g, d
		}
		d++
	}

	for i < n {
		if b>>i&1 > 0 {
			s = append(s, i+1)
		}
		i++
	}

	P(len(s), c)
	for _, v := range s {
		P(v)
	}
}