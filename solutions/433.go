package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
const O = 2e6
func main() {
	var (
		u    = [2 * O]int{O: 1}
		p, r int
		s    = b.NewScanner(Stdin)
	)

	s.Buffer(make([]byte, O), O)

	s.Scan()
	s.Scan()
	for _, v := range s.Text() {
		p--
		if v < 98 {
			p += 2
		}
		r += u[p+O]
		u[p+O]++
	}

	Print(r)
}