package main
import . "fmt"
func main() {
	var n, a, b, c int

	Scan(&n, &a, &b, &c)
	z := a + b + c - n
	x := z - b
	if x < 0 {
		x = 0
	}
	y := z - c
	if y < 0 {
		y = 0
	}
	z -= x + y
	a -= x + y
	b -= y + z
	c -= x + z
	if z < 0 || a < 0 || b < 0 || c < 0 || x+y+z+a+b+c != n {
		Print("NO")
		return
	}

	Println(`YES
`, x, a, y, b, z, c)
}