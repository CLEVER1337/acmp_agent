package main
import . "fmt"
func main() {
	k := 0
	a := 2

	Scan(&k)
	if k > 4 {
		a = 4 + (k-5)/5*2 + k/37 + k/44*2 - k/45
	}
	if k == 39 || k > 47 && k < 50 {
		a += 2
	}

	Print(k + a)
}