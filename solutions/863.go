package main
import . "fmt"
func F(n int) []int {
	e := make([]int, n)
	if n > 1 {
		e = e[:0]
		for _, v := range F(n / 2) {
			e = append(e, 2*v+1)
		}
		n++
		for _, v := range F(n / 2) {
			e = append(e, 2*v)
		}
	}
	return e
}

func main() {
	n := 0

	Scan(&n)
	for _, v := range F(n) {
		Println(v)
	}
}