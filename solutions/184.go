package main
import (
	. "fmt"
	. "sort"
)
func main() {
	var (
		t                      [5e4]int
		o, l, i, K, w, z, y, u int
	)

	Scanln(&K)
	for l < K {
		Scanf(`%02d.%02d. %02d:%02d
`, &w, &z, &y, &u)
		w--
		for 1 < z {
			z--
			w += []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}[z-1]
		}
		t[l] = w*1440 + y*60 + u
		l++
	}

	Ints(t[:K])
	for i < K {
		l = t[i+1] + 1
		z = t[i]
		for z < l {
			u = (z / 1440) * 1440
			y = u + 1440
			w = u + 600
			u += 1080
			if w < z {
				w = z
			}
			if u > l {
				u = l
			}
			if u > y {
				u = y
			}
			if w < u {
				o += u - w
			}
			z = y
		}
		i += 2
	}

	Printf("%d:%02d", o/60, o%60)
}