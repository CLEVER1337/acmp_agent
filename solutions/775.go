package main
import . "fmt"
func main() {
	n := ""
	m := n
	Scan(&n, &m)
	if m < "1" {
		Print("NO")
	} else {
		l := len(n) - 1
		Print(n[:l], n[l]-47)
	}
}