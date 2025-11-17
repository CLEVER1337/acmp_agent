package main
import . "fmt"
func main() {
	var (
		e, q [8]int
		s    = ""
		w    = s
		o    = 7
		i    = 1
	)

	Scan(&s)
	for i < 8 {
		e[i] = -1
		i++
	}

	i = 2
	for i < 8 {
		h := 2
		for h < 5 && i-h >= 0 {
			z := i - h
			t := s[z:i]
			n := len(t)
			x := 0
			a := t[0]
			b := t[1]
			if n == 2 && a == b {
				x = 2
			}
			if n == 3 {
				c := t[2]
				if a == b || b == c || a == c {
					x = 2
				}
				if a == b && b == c {
					x = 3
				}
			}
			if n == 4 {
				c, d := t[2], t[3]
				if a == c && a != b && a != d && b != d ||
					b == d && a != b && b != c && a != c {
					x = 2
				}
				if a == b && c == d && a != c ||
					a == b && b == c && a != d ||
					a == c && b == d && a != b ||
					b == c && c == d && a != b {
					x = 3
				}
				if a == d && b == c && a != b {
					x = 4
				}
				if a == b && b == c && c == d {
					x = 5
				}
			}
			if e[z]+x > e[i] {
				e[i] = e[z] + x
				q[i] = h
			}
			h++
		}
		i++
	}

	for o > 0 {
		l := q[o]
		w = s[o-l:o] + "-" + w
		o -= l
	}

	Println(w[:len(w)-1], e[7])
}