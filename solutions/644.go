package main
import (
	. "fmt"
	. "math/bits"
)
type U = uint64
var (
	q    [24][1 << 16]int32
	w    [24][1 << 16]uint16
	n    U
	i, p int
	F    = OnesCount64
)
func main() {
	for i < 24 {
		j := 1<<16 - 1
		for j >= 0 {
			k := j + OnesCount16(uint16(j)) + i
			if k > 65534 {
				q[i][j] = int32(k)
				w[i][j] = 1
			} else {
				q[i][j] = q[i][k]
				w[i][j] = w[i][k] + 1
			}
			j--
		}
		i++
	}

	Scan(&n, &p)
	for {
		m := n >> 16
		j := n & 65535
		i = F(m)
		if int(w[i][j]) > p {
			break
		}
		p -= int(w[i][j])
		n = m<<16 + U(q[i][j])
	}

	for p > 0 {
		n += U(F(n))
		p--
	}

	Print(n)
}