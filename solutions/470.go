package main
import (
	b "bufio"
	. "fmt"
	. "os"
	. "strconv"
	. "strings"
)
func main() {
	var (
		a          [4]int
		f          [101][101]int
		h, w, n, i int
		s          = b.NewScanner(Stdin)
	)

	Scan(&h, &w, &n)
	for i < h {
		i++
		x := 0
		for x < w {
			x++
			Scan(&f[i][x])
			q := f[i-1]
			f[i][x] += f[i][x-1] + q[x] - q[x-1]
		}
	}
	s.Scan()
	for 0 < n {
		s.Scan()
		t := Split(s.Text(), " ")
		for i, s := range t {
			a[i], _ = Atoi(s)
		}
		v := f[a[0]-1]
		w = a[1] - 1
		q := f[a[2]]
		Println(q[a[3]] - q[w] - v[a[3]] + v[w])
		n--
	}
}