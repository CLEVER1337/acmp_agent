package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strconv"
)
func main() {
	var (
		N, k, q int
		r       = b.NewScanner(Stdin)
		o       = b.NewWriter(Stdout)
		W       = o.WriteString
	)
	r.Split(b.ScanWords)

	Scanln(&N, &k, &q)
	for q > 0 {
		q--
		r.Scan()
		m, _ := Atoi(r.Text())
		w := N
		for m >= k && m%k > 0 {
			x := w / k
			z := (w - x*k + x - 1) / x
			y := m / k
			g := (m - y*k + y - 1) / y
			if g < z {
				z = g
			}
			if z < 1 {
				z = 1
			}
			w -= z * x
			m -= z * y
		}
		W(Itoa(N - w + m/k))
		W(`
`)
	}
	o.Flush()
}