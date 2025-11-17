package main
import . "fmt"
func main() {
	n := 0
	t := 1

	Scan(&n)
	for t <= n/2 {
		t *= 2
	}

	Print(n - t)
}