package main
import . "fmt"
func main() {
	b := 1
	p := 1
	s := ""
	Scan(&s)
	for b <= len(s) {
		Print(s[b-1 : b])
		p, b = b, p+b
	}
}