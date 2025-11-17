package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	r := b.NewScanner(Stdin)
	r.Scan()
	var (
		a, w, c, l, e int
		v             = "ERROR"
		N             = "NO"
		n             = -1
		s             = r.Text()
		o             = len(s) - 6
		F             = func(u *int) {
			n++
			o += 2
			m := 1
			if s[n] == 45 {
				m = -1
				n++
			}
			l = n
			for n < o && s[n] > 47 && s[n] < 58 {
				*u = *u*10 + int(s[n]-48)
				n++
			}
			*u = *u * m
			if n == l {
				e = 1
			}
		}
	)

	if o < -1 {
		s += v
		e = 1
	}

	F(&a)
	d := s[n]

	F(&w)
	if s[n] != 61 {
		e = 1
	}

	F(&c)
	if n < o {
		e = 1
	}

	if e < 1 {
		if d == 45 {
			v = N
			a -= w
		}
		if d == 43 {
			v = N
			a += w
		}
		if d < 43 {
			v = N
			a *= w
		}
		m := a == c
		if d == 47 {
			v = N
			m = w != 0 && a/w == c && a%w < 1
		}
		if m {
			v = "YES"
		}
	}

	Print(v)
}