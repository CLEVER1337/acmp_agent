package main
import . "fmt"
func main() {
	b := 0
	g := 0

	Scan(&b, &g)
	for b > 0 || g > 0 {
		i := 2
		if b > 0 {
			Print("B")
			b--
		}
		for g*i > 0 {
			Print("G")
			g--
			i--
		}
	}
}