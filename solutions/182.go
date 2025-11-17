package main
import . "fmt"
func main() {
	var a, b, c, d, e, f int

	Scan(&a, &e, &b, &f, &c, &d)
	k := b - a
	o := f - e
	l := k*k + o*o
	k = b - c
	o = f - d
	m := k*k + o*o
	k = c - a
	o = d - e
	o = k*k + o*o
	if m > l && m > o {
		b, a = a, b
		f, e = e, f
	}
	if l > m && l > o {
		b, c = c, b
		d, f = f, d
	}

	Print(a-b+c, e-f+d)
}