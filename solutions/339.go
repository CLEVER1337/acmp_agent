package main
import . "fmt"
func F(y, h int) int {
	a := (14 - h) / 12
	y += 4800 - a
	return (153*(h+12*a-3)+2)/5 + 365*y + y/4 - y/100 + y/400 - 32045
}

func main() {
	var a, b, c, d, e, f int

	Scanf(`%d.%d.%d
%d.%d.%d`, &a, &c, &e, &b, &d, &f)

	Print(F(f, d) + b - F(e, c) - a + 1)
}