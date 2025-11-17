package main
import . "fmt"
func main() {
	var (
		s                string
		q                []int
		m                [400][400]bool
		v                [501][]int
		n, k, j, i, l, z int
		P                = Println
		S                = Scan
	)

	S(&n, &k)
	N := n
	for i < n {
		S(&s)
		j = 0
		for j < n {
			m[i][j] = s[j] == 45
			j++
		}
		i++
	}

	for l < k {
		S(&j)
		for {
			S(&j)
			if j == n {
				break
			}
			v[l] = append(v[l], j-1)
		}
		q = append(q, l)
		l++
	}

	l = len(q)
	for l > 1 {
		l--
		k = q[l]
		q = q[:l]
		l--
		h := q[l]
		q = q[:l]
		i = 0
		j = 0
		for i < len(v[k]) && j < len(v[h]) {
			if m[v[h][j]][v[k][i]] {
				k, h = h, k
				i, j = j, i
			}
			for i < len(v[k]) && m[v[k][i]][v[h][j]] {
				v[n] = append(v[n], v[k][i])
				i++
			}
			v[n] = append(v[n], v[h][j])
			j++
		}
		for i < len(v[k]) {
			v[n] = append(v[n], v[k][i])
			i++
		}
		for j < len(v[h]) {
			v[n] = append(v[n], v[h][j])
			j++
		}
		q = append(q, n)
		l++
		n++
	}

	n = q[0]
	P(1)
	for z < len(v[n]) {
		P(v[n][z] + 1)
		z++
	}
	P(N)
}