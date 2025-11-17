package main
import . "fmt"
func main() {
	var a, b, c int
	s := ""
	Scan(&s)

	for _, v := range s {
		if v < 98 {
			a++
		}
		if v == 98 {
			b += a
		}
		if v == 99 {
			c += b
		}
	}

	Print(c)
}