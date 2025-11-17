package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		d [101]Int
		s = ""
		i = 0
	)

	Scan(&s)
	n := len(s)
	if n > 0 {
		d[0] = *NewInt(1)
		for i < n {
			i++
			d[i].Add(&d[i], &d[i-1])
			if i > 1 {
				m := int(s[i-2]-48)*10 + int(s[i-1]-48)
				if m > 9 && m < 34 {
					d[i].Add(&d[i], &d[i-2])
				}
			}
		}

		Print(&d[n])
	}
}