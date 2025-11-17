package main
import . "fmt"
var (
	s       = ""
	a       = [11]int{-1}
	f, m, q [512]int
	v       []rune
	c, i    int
)

func F(l, r int) int {
	k := 0
	j := r
	for j >= l {
		switch s[j] {
		case 40:
			k++
		case 41:
			k--
		case 124:
			if k == 0 {
				return F(l, j-1) | F(j+1, r)
			}
		}
		j--
	}
	j = r
	for j >= l {
		switch s[j] {
		case 40:
			k++
		case 41:
			k--
		case 38:
			if k == 0 {
				return F(l, j-1) & F(j+1, r)
			}
		}
		j--
	}
	if s[l] == 33 {
		return 1 ^ F(l+1, r)
	}
	if s[l] == 40 && s[r] == 41 {
		return F(l+1, r-1)
	}
	if l == r {
		return m[s[l]]
	}
	return -1
}

func main() {
	Scan(&s)
	for _, h := range s {
		if h > 96 && h < 123 && f[h] < 1 {
			f[h] = 1
			v = append(v, h)
			c++
		}
	}

	for i < 1<<c {
		j := 0
		h := 97
		for h < 123 {
			if f[h] > 0 {
				m[h] = 0
				if 1<<j&i > 0 {
					m[h] = 1
				}
				j++
			}
			h++
		}
		q[i] = F(0, len(s)-1)
		i++
	}

	for {
		j := 0
		for a[j] == c-1 {
			a[j] = 0
			j++
		}
		a[j]++
		i = 0
		for i < 1<<c {
			k := 0
			h := 97
			for h < 123 {
				if f[h] > 0 {
					m[h] = 0
					if 1<<k&i > 0 {
						m[h] = 1
					}
					k++
				}
				h++
			}
			if (((m[v[a[0]]]+m[v[a[1]]]+m[v[a[2]]])/2+m[v[a[3]]]+m[v[a[4]]])/2+(m[v[a[5]]]+m[v[a[6]]]+m[v[a[7]]])/2+m[v[a[8]]])/2 != q[i] {
				break
			}
			i++
		}
		if i == 1<<c {
			Printf("<<<%c%c%c>%c%c><%c%c%c>%c>", v[a[0]], v[a[1]], v[a[2]], v[a[3]], v[a[4]], v[a[5]], v[a[6]], v[a[7]], v[a[8]])
			return
		}
	}
}