package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)
	c := n * 3 % 4

	j := 1
	for n >= j {
		q := j
		w := 0
		e := j
		r := n
		if j&1 > 0 {
			q = 0
			w = j
			e = n
			r = j
		}
		if c < 1 {
			q = e
			w = r
			n--
		}
		j++
		Println(j/2, j&1+1, q, w)
		c--
	}
}