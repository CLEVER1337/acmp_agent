package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)

	if n > 2 {
		n *= (n-1) * (n-2)
	} 

	Print(n)
}