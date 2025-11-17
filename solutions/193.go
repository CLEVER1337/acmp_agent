package main
import . "fmt"
func main() {
	var (
		L, R, U, D       [256]int
		n, m, k, i, z, l int
	)

	Scan(&n, &m, &k)
	for i <= k {
		L[i] = m + 1
		U[i] = n + 1
		i++
	}

	for z < n {
		x := 0
		for x < m {
			Scan(&i)
			if i > 0 {
				q := n - z
				I := 0
				for I < 2 {
					if x < L[i] {
						L[i] = x
					}
					if x > R[i] {
						R[i] = x
					}
					if q < U[i] {
						U[i] = q
					}
					if q > D[i] {
						D[i] = q
					}
					i = 0
					I++
				}
			}
			x++
		}
		z++
	}

	for l < k {
		l++
		i = l
		if L[l] > m {
			i = 0
		}
		Println(L[i], U[i]-1, R[i]+1, D[i])
	}
}