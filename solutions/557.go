package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strconv"
	. "strings"
)
type T [130]int
func main() {
	var (
		u             T
		m, n, a, c, p int
		s             = b.NewReader(Stdin)
	)

	Scan(&m, &n, &a, &c, &p)

	u[a-1] = 1
	for 0 < m {
		var (
			q    [130]T
			w    T
			i, j int
		)
		for i < n {
			y, _ := s.ReadString('\n')
			if len(y) > 2 {
				for l, v := range Fields(y) {
					e, _ := Atoi(v)
					q[i][l] = e % p
				}
				i++
			}
		}
		for j < n {
			a = 0
			i = 0
			for i < n {
				a = (a + u[i]*q[i][j]) % p
				i++
			}
			w[j] = a
			j++
		}
		u = w
		m--
	}

	Print(u[c-1])
}