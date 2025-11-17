package main
import . "fmt"
func main() {
	var f, p, i int

	Scan(&f, &p)
	m := f
	for i < 4 {
		m += ((m-f)/p + 1) * (f - p)
		i++
	}

	Print(m)
}