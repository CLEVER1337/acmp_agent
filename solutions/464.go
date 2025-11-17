package main
import . "fmt"
func main() {
	n := 0
	r := 0
    
	Scan(&n)
	for n > 1 {
		k := 1
		for k < n {
			k <<= 1
		}
		n -= k >> 1
		r++
		r %= 3
	}

	Print(r)
}