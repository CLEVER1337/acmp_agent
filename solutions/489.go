package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		n, k, l, j, i int
		w             [1e5]int
		f             = map[int]int{}
		r             = b.NewReader(Stdin)
		S             = Fscan
	)

	Scan(&n, &k)
	q := make([]int, n)
	for l < n {
		S(r, &q[l])
		l++
	}

	for j < n-1 {
		S(r, &w[j])
		j++
	}

	for i < k {
		S(r, &j)
		f[j]++
		i++
	}

	for _, c := range w {
		for j := range q {
			if q[j] == c {
				q = append(q[:j], q[j+1:]...)
				goto A
			}
		}
		if c < 0 {
			c = -c
		}
		for j := range q {
			i = q[j]
			if i < 0 {
				i = -i
			}
			if i == c && f[c] > 0 {
				q = append(q[:j], q[j+1:]...)
				break
			}
		}
	A:
	}

	l = q[0]
	u := l > 0

	if l < 0 {
		l = -l
	}

	i = f[l]
	if i&1 > 0 {
		u = !u
	}

	if !u {
		l = -l
	}

	Print(l)
}