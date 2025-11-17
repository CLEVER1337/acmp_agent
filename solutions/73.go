package main
import . "fmt"
func main() {
	s := ""

	Scan(&s)
	for i, c := range s {
		n := c - 7
		if c > 47 && c < 58 {
			n = c
		}
		n -= rune(i) + 49
		for n <= 0 {
			n += 27
		}
		if n == 27 {
			n -= 91
		}

		Printf("%c", 96+n)
	}
}