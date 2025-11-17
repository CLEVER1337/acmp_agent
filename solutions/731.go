package main
import . "fmt"
func main() {
	var (
		g, o, p                [31]int
		n, u, v, m, k, i, l, z int
	)

	Scan(&n)
	for i < n {
		Scanf(`
%c %d`, &p[i], &g[i])
		m += g[i]
		i++
	}
	for z < n {
		i = g[z] * 100
		o[z] = i / m
		k += i / m
		if i%m > 0 {
			v++
			if p[z] < 44 {
				u++
				v--
			}
		} else {
			p[z] = 48
		}
		z++
	}
	for l < n {
		if k < 100 && (p[l] == 45 && u < v || p[l] < 44) {
			o[l]++
			k++
			if p[l] < 44 {
				v--
			}
		}
		Println(o[l])
		l++
	}
}