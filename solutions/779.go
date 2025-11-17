package main
import . "fmt"
func main() {
	n := 0
	x := 0

	Scan(&n)
	n /= 2 
	for -1 < n {
		Scan(&x)
	n--
	}

	Print(x)
}