package main
import (
	. "fmt"
	. "strings"
)
func main() {
	var (
		p = map[byte]string{
			48:  "0",
			49:  "1",
			50:  "2",
			51:  "3",
			52:  "4",
			53:  "5",
			54:  "6",
			55:  "7",
			56:  "8",
			57:  "9",
			97:  "0123",
			98:  "1234",
			99:  "2345",
			'd': "3456",
			'e': "4567",
			'f': "5678",
			'g': "6789",
			63:  "0123456789"}
		x = ""
		z = x
		r = 1
		i = 0
		C = Contains
	)
    
	Scan(&x, &z)
	for i < len(x) {
		g := 0
		d := 48
		for d < 58 {
			s := string(d)
			if C(p[x[i]], s) && C(p[z[i]], s) {
				g++
			}
			d++
		}
		r *= g
		i++
	}

	Print(r)
}