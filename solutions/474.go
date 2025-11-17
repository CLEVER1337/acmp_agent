package main
import . "fmt"
func main() {
	s := ""
	i := 0

	Scan(&s)
	n := []byte(s)
	for i < len(s) {
		n[i] -= 48
		i++
	}

	i = len(n)
	for i > 0 {
		i--
		if n[i] > 0 {
			n[i]--
			break
		} else {
			n[i] = 9
		}
	}

	i = 0
	for len(n) > 0 {
		r := 0
		var t []byte
		for _, d := range n {
			r = r*10 + int(d)
			q := r / 3
			r %= 3
			if q > 0 || len(t) > 0 {
				t = append(t, byte(q))
			}
		}
		if r == 2 {
			i = 1 - i
		}
		n = t
	}

	Print(i)
}