package main
import . "fmt"
func main() {
	var (
		a                      [100][100]int
		n, b, i, j, k, l, z, N int
	)
	N = 1e9

	Scan(&n)
	for i < n {
		j = 0
		for j < n {
			Scan(&b)
			if b == 0 {
				b = N
			}
			a[i][j] = b
			j++
		}
		i++
	}

	for k < n {
		i = 0
		for i < n {
			j = 0
			for j < n {
				b = a[i][k]
				m := a[k][j]
				if b < N && m < N && b+m < a[i][j] {
					a[i][j] = b + m
				}
				j++
			}
			i++
		}
		k++
	}

	for l < n {
		j = 0
		for j < n {
			k = 0
			for k < n {
				if a[l][k] < N && a[k][j] < N && a[k][k] < 0 {
					a[l][j] = -N
				}
				k++
			}
			j++
		}
		l++
	}

	for z < n {
		j = 0
		for j < n {
			b = 1
			k = a[z][j]
			if k == -N {
				b = 2
			}
			if z != j && k == N {
				b = 0
			}
			Print(b, " ")
			j++
		}
		z++
	}
}