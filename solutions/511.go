package main
import . "fmt"
func main() {
	n := 0

	Scan(&n)
	if n > 145 {
		Print("NO")
		return
	}

	n = n*5 - 5
	Print(n/60, n%60)
}