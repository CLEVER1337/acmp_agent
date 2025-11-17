package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		d             [501][501]Int
		t             Int
		n, k, m, i, j int64
		N             = NewInt
		q             = N(1)
	)

	Scan(&n, &k)
	d[1][1] = *q

	for i < n {
		j = 0
		for j < k {
			j++
			z := &d[i][j]
			o := d[i+1]
			d[i+1][j].Add(&o[j], q.Mul(z, N(j)))
			if j < k {
				d[i+1][j+1].Add(&o[j+1], z)
			}
		}
		i++
	}

	for m < k {
		m++
		t.Add(&t, &d[n][m])
	}

	Print(&t)
}