package main
import . "fmt"
func main() {
	var (
		n, m, p, i, j int
		s             = "YES"
		e             [100]string
		S             = Scan
	)

	S(&n, &m)
	for j < n {
		S(&e[j])
		j++
	}

	for i < n {
		j = 0
		for j < m {
			l := "."
			S(&p)
			if p > 3 {
				l += "R"
			}
			if p%2 == 1 {
				l += "B"
			}
			switch p {
			case 2, 3, 6, 7:
				l += "G"
			}
			f := 0
			for f < len(l) {
				if e[i][j] == l[f] {
					p = 9
				}
				f++
			}
			if p != 9 {
				s = "NO"
			}
			j++
		}
		i++
	}

	Print(s)
}