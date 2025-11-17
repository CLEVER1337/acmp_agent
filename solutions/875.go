package main
import . "fmt"
func main() {
	var (
		n, m, k, i int
		a, b       [100]string
	)

	Scan(&n, &m, &k)
	for i < n {
		Scan(&a[i])
		b[i] = a[i]
		i++
	}

	for 0 < k {
		i = 0
		for i < n {
			d := (i + 1) % n
			u := i
			if u < 1 {
				u = n
			}
			u--
			j := 0
			for j < m {
				l := j
				if l < 1 {
					l = m
				}
				l--
				r := (j + 1) % m
				t := a[u][l] + a[u][j] + a[u][r] + a[i][l] + a[i][r] + a[d][l] + a[d][j] + a[d][r]
				if t != 104 {
					s := "."
					if t == 100 {
						s = "*"
					}
					b[i] = b[i][:j] + s + b[i][j+1:]
				}
				j++
			}
			i++
		}
		i = 0
		for i < n {
			a[i] = b[i]
			i++
		}
		k--
	}

	for k < n {
		Println(b[k])
		k++
	}
}