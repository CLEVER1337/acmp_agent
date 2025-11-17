package main
import . "fmt"
func main() {
	n := 0
	o := 0
	s := ""
	Scan(&n, &s)

	for 0 < n {
		n--
		if s[n] > 48 {
			o++
		}
	}

	s = ""
	for o > 0 {
		s = Sprint(o&1) + s
		o >>= 1
	}
	if s == "" {
		s = "0"
	}
	Print(s)
}