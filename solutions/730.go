package main
import . "fmt"
type A int16
func main() {
	var (
		h                []int
		Y, V, C, I       [22]int
		n, m, u, v, l, o int
		q                A = 1 << 14
		a                A
		P                = Println
	)

	Scan(&n, &m)
	if n > 1 {
		for l < m {
			Scan(&u, &v, &C[l])
			Y[l] = u - 1
			V[l] = v - 1
			I[l] = l + 1
			l++
		}

		z := 1 << n
		d := make([]A, z)
		for i := range d {
			d[i] = q
		}
		d[1] = 0

		for o < z {
			if d[o] != q {
				for i, e := range Y {
					if o>>e&1 > 0 {
						m = o | 1<<V[i]
						x := d[o] + A(C[i])
						if x < d[m] {
							d[m] = x
						}
					}
				}
			}
			o++
		}

		z--
		c := z
		for c != 1 {
			l = 0
			m = 0
			n = 0
			for i := range Y {
				u = c ^ 1<<V[i]
				if d[u]+A(C[i]) == d[c] {
					l = I[i]
					m = u
					n = 1
					break
				}
			}
			h = append(h, l)
			c = m
		}
		a = d[z]
		l = len(h)
	}

	P(a, l)
	for l > 0 {
		l--
		P(h[l])
	}
}