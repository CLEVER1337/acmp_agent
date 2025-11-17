package main
import . "fmt"
func main() {
	var n, s, a int

	Scan(&n)
	if n > 3 {
		for a < n/4 {
			a++
			b := a
			for b <= (n-a)/3 {
				s += (n-a-b)/2 - b + 1
				b++
			}
		}
	}

	Print(s)
}