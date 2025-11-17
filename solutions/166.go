package main
import . "fmt"
func main() {
	n := 0
	k := 0
	y := 1
	Scan(&k, &n)

	a := [3]int{k, 0, 0}

	for y < n {
		R := a[0] + a[1] + a[2]
		v := 0
		if R > 0 {
			w := R / 5
			b := w
			for b >= 0 && w-b < 6 {
				t := 5*((R-5*b)/3) + 9*b
				if t > v {
					v = t
				}
				b--
			}
		}
		a[2], a[1], a[0] = a[1], a[0], v
		y++
	}

	Print(a[0] + a[1] + a[2])
}