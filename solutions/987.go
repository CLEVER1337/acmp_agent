package main
import . "fmt"
func main() {
	var (
		s             = ""
		p             = s
		a             = 1e4
		x, i, n, u, t float64
		S = Scan
		P = Print
	)

	S(&p, &p)
	for i < 4 {
		S(&s, &s)
		if s != "out" {
			S(&s, &s)
			Sscan(s[5:], &t)
			if a > t {
				a = t
			}
			if x < t {
				x = t
			}
			u += t
			n++
		}
		i++
	}

	i = 4 - n
	P("Ping statistics for ", p+`:
Packets: Sent = 4 Received = `, n, " Lost = ", i, " (", i*25, `% loss)
`)
	if n > 0 {
		P(`Approximate round trip times:
Minimum = `, a, " Maximum = ", x, " Average = ", int(u/n+0.5))
	}
}