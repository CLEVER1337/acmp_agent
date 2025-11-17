package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strconv"
)
func main() {
	s := b.NewScanner(Stdin)
	s.Split(b.ScanWords)

	var (
		F = func() int {
			s.Scan()
			v, _ := Atoi(s.Text())
			return v
		}
		h    = map[any]int{}
		u    []byte
		l, r int
		p    = F()
		o    = F()
		w    = F()
		P    = Println
		H    = func() {
			u = u[:0]
			i := 0
			for i < p {
				u = AppendInt(u, int64(F()), 10)
				i++
			}
		}
	)

	for o > 0 {
		k := F()
		H()
		h[string(u)] = k
		o--
	}

	for w > 0 {
		H()
		v := h[string(u)]
		if v > 0 {
			l++
			P(v)
		} else {
			r++
			P("-")
		}
		w--
	}

	Print("OK=", l, " BAD=", r)
}