package main
import . "fmt"
func main() {
	n := 0
	k := 0
	Scan(&n, &k)
	Print((k + 1) * ((n-2)*k + 2) / 2)
}