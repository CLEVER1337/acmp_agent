package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)
	Print(n&1*2, n&1*(n+2))
}