package main
import . "fmt"
func main() {
	n := 0
	a := "0"

	Scan(&n)
	for n > 1 {
		var (
			v [10]int
			p = -1
			f = p
			i = 10
			q = ""
		)
		for _, c := range a {
			v[c-48]++
		}

		for i > 0 {
			i--
			if v[i] < 1 {
				p = i
			}
		}

		i = int(a[0] - 48)
		if 1 > i {
			i = 1
		}
		for i < 10 {
			if v[i] < 1 {
				f = i
				break
			}
			i++
		}

		if f < 0 {
			for i > 1 {
				i--
				if v[i] < 1 {
					f = i
				}
			}
			q = Sprint(p)
		}

		r := []rune(a)
		i = 1
		for i < len(a) {
			r[i] = rune(p + 48)
			i++
		}

		r[0] = rune(f + 48)
		a = string(r) + q
		n--
	}

	Print(a)
}