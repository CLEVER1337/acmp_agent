package main
import . "fmt"

var (
	s    = ""
	o, y int
	E    = ' '
	c    = E
	w    = "NO"
	p    = w
)

func F() {
	c = E
	if o < len(s) {
		c = rune(s[o])
		o++
	}
}

func main() {
	Scan(&s)

	F()
	for {
		e := ""

		if c < 65 || c > 90 {
			goto A
		}

		e += string(c)
		F()

		if c > 96 && c < 123 {
			e += string(c)
			F()
		}

		if c > 47 && c < 58 {
			if c < 49 {
				goto A
			}
			if c == 49 {
				F()
				if c < 48 || c > 57 {
					goto A
				}
			}
			F()
			for c > 47 && c < 58 {
				F()
			}
		}

		if y > 0 && p == e {
			goto A
		}
		y = 1
		p = e

		if c == E {
			break
		}
	}

	if c == E {
		w = "YES"
	}
A:
	Print(w)
}