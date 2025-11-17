package main
import . "fmt"
func main() {
	var n, b, c int

	Scan(&n, &b, &c)
	for n > 1 {
		b, c = c-b, b
		n--
	}

	Print(b, c)
}