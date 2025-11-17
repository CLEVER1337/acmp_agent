package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)
	Print(n/6+(7-n%6)*((n%6+5)/6), n*6)
}