package main
import . "fmt"
type S string
func main() {
	var (
		q             [11]S
		n, k, p, j, i int
		s             S
		P             = Printf
	)

	Scan(&n, &k, &p, &s)
	v := []S{s}
	for j < n {
		Scan(&q[j])
		j++
	}

	for i < k {
		s = ""
		j = 0
		for j < len(v[i]) {
			s += q[int(v[i][j]-65)]
			j++
		}
		if len(s) > p {
			s = s[:p]
		}
		j = 0
		h := len(v)
		for j < h {
			if v[j] == s {
				if i < k {
					k -= j
					k %= h - j
					k += j
				}
				goto A
			}
			j++
		}
		v = append(v, s)
		i++
	}
A:

	if len(v[k]) >= p {
		P("%c", v[k][p-1])
	} else {
		P("-")
	}
}