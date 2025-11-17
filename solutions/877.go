package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strings"
)
func main() {
	var (
		w [800]string
		s = b.NewScanner(Stdin)
		j = 0
	)

	for s.Scan() {
		w[j] = s.Text()
		j++
	}

	p := Fields(w[0])
	u := p[len(p)-3]
	for i, z := range w[1 : j-1] {
		k := "Fedya"
		if i%2 > 0 {
			k = u
		}
		x := z[Index(z, ": ")+2:]
		j = len(x) - 1
		l := x[j]
		q := x + ","
		if l == 46 {
			q = x[:j] + ","
		}
		if l == 33 || l == 63 {
			q = x[:j] + string(l)
		}
		Printf(`"%s" --- skazal %s.
`, q, k)
	}
}