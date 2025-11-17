package main
import . "fmt"
func main() {
	var n, a, b, k int

	Scan(&n, &a)
	for 1 < n {
		Scan(&b)
		if a != b-1 {
			k++
		}
		a = b
		n--
	}

	Print(k)
}