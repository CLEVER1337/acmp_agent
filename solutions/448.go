package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	w := b.NewWriter(Stdout)
	N := 0
	Scan(&N)

	for N > 1 {
		p := N + 1
		for {
			i := 2
			if p < 2 {
				goto A
			}
			for i*i <= p {
				if p%i == 0 {
					goto A
				}
				i++
			}
			break
		A:
			p++
		}
		d := p - N
		i := 0
		for d+i < N-i {
			Fprintln(w, d+i, N-i)
			i++
		}
		N = d - 1
	}
	w.Flush()
}