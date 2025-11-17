package main
import . "fmt"
func main() {
	var (
		r, f, a, p [1e5]int
		n, l, u, i int
		j          = 1
		x          = 1000
	)

	Scan(&n)
	for l < n {
		Scan(&a[l])
		l++
	}

	o := a[0]
	for _, v := range a {
		if v > o {
			o = v
		}
	}

	p[0] = a[0]
	for j < n {
		l = p[j-1]
		if a[j] > l {
			l = a[j]
		}
		p[j] = l
		j++
	}

	for _, v := range a {
		if v > 0 && v < 1001 {
			f[v]++
		}
	}

	for x >= 0 {
		r[x] = u
		u += f[x]
		x--
	}

	u = 1e9
	for i < n-1 {
		l = a[i]
		if l%10 == 5 && a[i+1] < l && i > 0 && p[i-1] >= o {
			x = r[l] + 1
			if x < u {
				u = x
			}
		}
		i++
	}

	if u == 1e9 {
		u = 0
	}

	Print(u)
}