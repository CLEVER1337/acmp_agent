package main
import . "fmt"
func main() {
	n := 0
	z := 26

	Scan(&n)
	for n > 1 {
		z--
		if n > 1<<z {
			n -= 1<<z - 1
		}
		n--
	}

	Printf("%c", 96+z)
}