package main
import . "fmt"
func main() {
	n := 0
	o := 2
	b := 2
	s := "LOSE"

	Scan(&n)
	for b < n {
		if o*o <= b+o {
			o++
		}
		b += o
	}
	if b != n {
		s = "WIN"
	}

	Print(s)
}