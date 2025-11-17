package main
import . "fmt"
func main() {
	b := 0
	P := Println

	Scan(&b)
	if b == 4 {
		P(2, 1, 0, 1)
	} else if b == 5 {
		P(1, 2, 0, 0, 2)
	} else if b > 6 {
		d := make([]int, b)
		d[0] = 2
		d[1] = 1
		d[b-5] = 1
		d[b-1] = b - 4
		for _, v := range d {
			P(v)
		}
	} else {
		P(-1)
	}
}