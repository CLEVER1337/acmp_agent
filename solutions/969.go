package main
import . "fmt"
func main() {
	n := 0
	m := 0
    
	Scan(&n, &m)
	r := 2 % m
	for 0 < n {
		r = r * r % m
		n--
	}

	Print(r)
}