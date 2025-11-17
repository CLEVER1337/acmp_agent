package main
import . "fmt"
type A [4e3]float64
func main() {
	d := A{1}
	N := 0
	Q := 0

	Scan(&N, &Q)
	for 0 < N {
		var w A
		s := 0
		for s <= Q {
			if d[s] > 0 {
				k := 1
				for k < 7 {
					if s+k <= Q {
						w[s+k] += d[s] / 6
					}
					k++
				}
			}
			s++
		}
		d = w
		N--
	}

	Print(d[Q])
}