package main
import . "fmt"
func main() {
	var (
		q                   = ""
		d                   = [11][2e3]int{{1}}
		n, m, k, a, j, i, v int
	)

	Scan(&n, &m, &k)
	for i < n {
		w := 0
		Scan(&q)
		for w < 1<<m {
			d[i+1][w] += d[i][w]
			j = 0
			for j < m {
				if q[j] > 88 && w&(1<<j) < 1 {
					d[i+1][1<<j|w] += d[i][w]
				}
				j++
			}
			w++
		}
		i++
	}

	for v < 1<<m {
		i = v
		j = 0
		for i > 0 {
			j += i & 1
			i >>= 1
		}
		if j == k {
			a += d[n][v]
		}
		v++
	}

	Print(a)
}