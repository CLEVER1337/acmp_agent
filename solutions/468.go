package main
import (
	. "fmt"
	. "math/big"
)
func main() {
	var (
		n, j, k int
		a       Int
	)

	Scan(&n)
	for (k+1)*k*(k-1)/6 < n {
		k++
	}

	n -= k * (k - 1) * (k - 2) / 6
	for (j+1)*j/2 < n {
		j++
	}

	for _, v := range []int{k, j, n - j*(j-1)/2 - 1} {
		t := NewInt(1)
		a.Add(&a, t.Lsh(t, uint(v)))
	}

	Print(&a)
}