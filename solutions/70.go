package main
import . "fmt"
func main() {
	s := ""
	n := 0
	i := 0

	Scan(&s, &n)
	v := s
	if n > 0 {
		for i < n-1 {
			if len(s) > 1023 {
				s = s[:1023]
				v = ""
			}
			s += v
			i++
		}
	} else {
		f := len(s)
		k := f / -n
		c := k
		i = 0
		for len(s) > k {
			if s[:c] != s[k:k+c] {
				i = 1
			}
			k += k
		}
		s = s[:c]
		if f%-n+i > 0 {
			s = "NO SOLUTION"
		}
	}

	Print(s)
}