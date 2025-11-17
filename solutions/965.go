package main
import . "fmt"
func main() {
	var (
		w, e                      [200]int
		n, m, x, a, u, z, l, i, j int
		P                         = Println
	)

	Scan(&n, &m)
	for i < m {
		Scan(&u, &z)
		u--
		z--
		w[i] = u
		e[i] = z
		i++
	}

	z = n
	for l < 1<<n {
		i = l
		u = 0
		for i > 0 {
			u += i & 1
			i >>= 1
		}
		for I, v := range w[:m] {
			if 1<<v&l == 1<<e[I]&l {
				goto A
			}
		}
		if u == z {
			a++
		}
		if u < z {
			z = u
			a = 1
			x = l
		}
	A:
		l++
	}

	P(z, a)
	for j < n {
		if 1<<j&x > 0 {
			P(j + 1)
		}
		j++
	}
}