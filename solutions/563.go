package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "sort"
)
type U uint
var (
	e, r U
	a    [1e5]U
)

func G(a U) U {
	r = 0
	i := 0
	for i < 32 {
		r = r<<1 | a&1
		a >>= 1
		i++
	}
	return r
}

func F(q, w int, z U) {
	if q != w && z > 0 {
		x := 0
		y := 0
		i := q
		for i < w {
			y++
			if a[i]&z < 1 {
				x++
				y--
			}
			i++
		}
		if (x&3)*(x-1)>>1&1 != (y&3)*(y-1)>>1&1 {
			e ^= z
		}
		F(q, q+x, z>>1)
		F(q+x, w, z>>1)
	}
}

func main() {
	var n, v, i int
	r := b.NewReader(Stdin)

	Scan(&n)
	for i < n {
		Fscan(r, &v)
		a[i] = G(U(v))
		e ^= a[i]
		i++
	}
	Slice(a[:n], func(i, j int) bool {
		return a[i] < a[j]
	})
	F(0, n, 1<<31)

	Print(int32(G(e)))
}