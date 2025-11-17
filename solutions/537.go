package main
import (
	. "fmt"
	. "sort"
)

var (
	q                      [16][16]bool
	d                      [16][7e4]int
	m                      [16]int
	N, M, K, s, j, i, l, k int
	P                      = Println
)

func main() {
	Scan(&N, &M, &K)
	for j < N {
		Scan(&m[j])
		j++
	}

	Ints(m[:N])
	for i < N {
		j = i + 1
		for j < N {
			a := m[i]
			b := m[j]
			for a > 0 {
				a, b = b%a, a
			}
			q[i][j] = b >= K
			q[j][i] = b >= K
			j++
		}
		i++
	}

	for l < 1<<N {
		i = 0
		for i < N {
			if l>>i&1 > 0 {
				if 1<<i^l < 1 {
					d[i][l] = 1
					break
				}
				j = 0
				for j < N {
					if q[i][j] {
						d[i][l] += d[j][1<<i^l]
					}
					j++
				}
			}
			i++
		}
		l++
	}

	j = 1<<N - 1
	for k < N {
		s += d[k][j]
		k++
	}

	l = -1
	if s < M {
		P(l)
		return
	}

	for j > 0 {
		i = 0
		s = 0
		for s < M {
			if l < 0 || q[i][l] {
				s += d[i][j]
			}
			i++
		}
		i--
		P(m[i])
		s -= d[i][j]
		M -= s
		j ^= 1 << i
		l = i
	}
}