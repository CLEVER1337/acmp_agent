package main
import . "fmt"
func main() {
	a := 0
	b := 0

	Scan(&a, &b)
	z := len(Sprint(a))
	j := z - 1
	for j <= z {
		h := make([]int, j)
		g := make([]int, j)
		k := 0
		p := 1
		i := 0
		for i < j {
			h[i] = a / p % 10
			p *= 10
			i++
		}
		for k < 1<<j {
			var n, l, r, s int
			for l < j {
				d := 0
				for d < 10 {
					g[l] = d
					u := l
					for {
						x := (u + j - b) % j
						t := 0
						if u > 0 {
							t = k >> (u - 1) & 1
						}
						e := k>>u&1*10 + h[u] - t - g[u]
						if (e < 0 || e > 9) || x == j-1 && e == 0 || x == l && e != g[l] {
							goto A
						}
						g[x] = e
						u = x
						if u == l {
							break
						}
					}
					goto B
				A:
					d++
				}
				break
			B:
				l++
			}
			i = j
			for i > 0 {
				i--
				n = n*10 + g[i]
			}
			for s < j {
				s++
				r = r*10 + g[(j+j-b-s)%j]
			}
			if n+r == a {
				Print(n)
				return
			}
			k++
		}
		j++
	}
}