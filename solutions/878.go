package main
import . "fmt"
func main() {
	var (
		a [26]int
		k, i int
		s = ""
		c = 65
		P = Println
	)

	Scan(&s)
	for c < 91 {
		t := -1
		i := 0
		for i < 26 {
			if s[i] >= byte(c) && (t < 0 || s[i] < s[t]) {
				t = i
			}
			i++
		}

		if t < 0 {
			P("NO")
			return
		}

		a[k] = t + 1
		k++
		s = s[:t] + "." + s[t+1:]
		c++
	}

	P("YES")
	for i < 26 {
		P(a[i])
		i++
	}
}