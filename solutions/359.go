package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)
	n = (n * n + 1) / 2 - 1
	Print(n / 9 * 10 + n % 9 + 1)
}