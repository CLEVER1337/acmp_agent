package main
import . "fmt"
func main() {
	var k, x, y, a int

	Scan(&k)
	for 0 < k {
		Scan(&x, &y, &a)
		f := 1
		if a > 2 {
			f = 0
			q := (y - 2) % a
			x %= a
			if x+q < 1 ||
				(x == 1 && (y-1)%a < 1 || y%a+q < 1) ||
				(x == 2 && y%a < 1) {
				f = 1
			}
		}
		Print(f)
		k--
	}
}