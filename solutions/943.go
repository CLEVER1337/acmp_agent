package main
import . "fmt"
func main() {
	var m, x, y int
	Scan(&m, &m, &y, &x)
	Print(y&1*(2*x-1-m) + m*y - x)
}