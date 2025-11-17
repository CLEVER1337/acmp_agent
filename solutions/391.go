package main
import . "fmt"
func main() {
	var r, v, i, x, m, h int
	s := ""

	Scan(&x, &m, &r, &v)
	for i < r {
		s += "0"
	i++
	}
	t := s

	for h != v {
		i = len(t) - 1
		for t[i] == 57 {
			t = t[:i] + "0" + t[i+1:]
		i--
		}

		if i >= 0 {
			t = t[:i] + string(t[i]+1) + t[i+1:]
		}

		if t == s {
			t = "NO SOLUTION"
			break
		}

		h = 0
		r = 1
		for _, d := range t {
			h += int(d-48)*r
			h %= m
			r *= x
			r %= m
		}
	}

	Print(t)
}