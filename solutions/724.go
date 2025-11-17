package main
import . "fmt"
func main() {
	var (
		p                [20][20]int
		a                [20]int
		n, m, b, i, v, q int
		P                = Println
	)

	Scan(&n, &m)
	for i < n {
		j := 0
		for j < m {
			Scan(&p[i][j])
			j++
		}
		i++
	}

	for v < m {
		i = 0
		for i < n {
			if p[i][v] < 1 {
				a[v] |= 1 << i
			}
			i++
		}
		v++
	}

	n = 1<<n - 1
	v = m + 1
	i = 1
	for i < 1<<m {
		var j, o, e int
		for j < m {
			if 1<<j&i > 0 {
				e |= a[j]
				o++
			}
			j++
		}
		if e == n && o < v {
			v = o
			b = i
		}
		i++
	}

	if v > m {
		P("Impossible")
		return
	}

	P(v)
	for q < m {
		if 1<<q&b > 0 {
			P(q + 1)
		}
		q++
	}
}