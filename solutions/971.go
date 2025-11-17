package main
import . "fmt"
func main() {
	x := 0
	y := 0
	Scan(&x, &y)

	switch int(1e9) {
	case x, -x, y, -y:
		Print("NO")
		return
	}

	z := x + 1
	if x < 0 {
		z -= 2
	}

	b := y + 1
	if y < 0 {
		b -= 2
	}

	Print(`YES
`, z, y, x, b, x*3-z-x, y*3-y-b)
}