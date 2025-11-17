package main
import . "fmt"
func main() {
	s := ""
	Scan(&s)
	var (
		e = 0
		a = -1
		b = a
		m = rune(s[0])
		n = m
		q = len(s)
		r = q
	)

	for _, v := range s {
		if v < m {
			m = v
		}
		if v > n {
			n = v
		}
	}

	for i, v := range s {
		if v == m {
			a = i
			if b > -1 && i-b+1 < q {
				r = i + 1
				q = r - b
				e = b
			}
		}
		if v == n {
			b = i
			if a > -1 && i-a+1 < q {
				r = i + 1
				q = r - a
				e = a
			}
		}
	}

	Print(s[e:r])
}