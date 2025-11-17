package main
import . "fmt"
func main() {
	a := "NO"
	s := ""
	i := 0
	c := map[any]int{40: 0, 41: 0, 91: 0, 93: 0, '{': 0, '}': 0}

	Scan(&s)
	n := len(s)
	if n < 1 {
		a = "YES"
	}
	for _, r := range s {
		c[r]++
	}
	if c[40] == c[41] && c[91] == c[93] && c[123] == c[125] {
		for i < n {
			var (
				t []rune
				h = s[i:] + s[:i]
				d = 1
			)
			for _, r := range h {
				switch r {
				case 40, 91, 123:
					t = append(t, r)
				case 41, 93, 125:
					if len(t) < 1 || t[len(t)-1] != map[rune]rune{41: 40, 93: 91, 125: 123}[r] {
						d = 0
					} else {
						t = t[:len(t)-1]
					}
				default:
					d = 0
				}
				if d < 1 {
					break
				}
			}
			if d > 0 && len(t) < 1 {
				a = "YES"
				break
			}
			i++
		}
	}

	Print(a)
}