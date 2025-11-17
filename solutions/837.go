package main
import . "fmt"
func main() {
	var k, a, b int

	Scan(&k)
	for 0 < k {
		s := "Yes "
		Scan(&a, &b)
		a--
		if a < 1 || b > a*(a-1)/2 {
			s = "No "
		}
		Print(s)
		k--
	}
}