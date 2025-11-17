package main
import . "fmt"
func main() {
	k := 0
	d := 1
	m := 1
	y := 0

	Scan(&k)
	a := k % 7
	for k > 0 {
		k--
		d++
		if d > 31 || d > 30 && (m == 4 || m == 6 || m == 9 || m == 11) || m == 2 && (d > 29 || d > 28 && y > 0) {
			d = 1
			m++
			if m > 12 {
				m = 1
				y++
			}
		}
	}

	Printf("%sday, %02d.%02d", []any{"Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun", "Mon"}[a], d, m)
}