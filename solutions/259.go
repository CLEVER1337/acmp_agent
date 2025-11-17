package main
import . "fmt"
func main() {
	var (
		r          [4e5]int
		l, v, n, i int
		s          = ""
	)

	Scan(&n, &s)
	u := []rune(s)
	j := n
	for i < j {
		j--
		u[i], u[j] = u[j], u[i]
		i++
	}

	s += string(u)
	m := n * 2
	i = 1
	for i < m {
		f := &r[i]
		a := r[i-l]
		if i <= v {
			if a > v-i+1 {
				a = v - i + 1
			}
			*f = a
		}
		for i+*f < m && s[*f] == s[i+*f] {
			*f++
		}
		a = i + *f - 1
		if a > v {
			l = i
			v = a
		}
		i++
	}

	for m > n {
		m--
		Println(r[m])
	}
}