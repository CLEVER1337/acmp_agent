package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		d                [300][300]int
		n, m, x, j, l, i int
		r                = b.NewReader(Stdin)
	)

	Scan(&n, &m)
	for l < n {
		j = 0
		for j < n {
			if l != j {
				d[l][j] = 1e6
			}
			j++
		}
		l++
	}

	for 0 < m {
		Fscan(r, &l, &j)
		l--
		j--
		d[l][j] = 0
		if d[j][l] == 1e6 {
			d[j][l] = 1
		}
		m--
	}

	for m < n {
		l = 0
		for l < n {
			j = 0
			for j < n {
				k := d[l][m] + d[m][j]
				if k < d[l][j] {
					d[l][j] = k
				}
				j++
			}
			l++
		}
		m++
	}

	for i < n {
		l = 0
		for l < n {
			m = d[i][l]
			if i != l && m < 1e6 && m > x {
				x = m
			}
			l++
		}
		i++
	}

	Print(x)
}