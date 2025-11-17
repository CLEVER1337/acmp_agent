package main
import (
	. "fmt"
	. "strings"
)
func main() {
	var (
		F    = "FALSE"
		s    = F
		n, k int
		C    = Contains
	)

	Scan(&s, &n, &k)
	for 0 < n {
		t := s
		j := 0
		a := ""
		for j < k {
			r := "0"
			Scan(&a)
			v := a[0]
			if a[1] == 61 && !C(a, F) {
				r = "1"
			}
			q := ""
			for i := range t {
				if t[i] == v && ((i < 1 || t[i-1] < 65 || t[i-1] > 90) &&
					t[i+1] < 65 || t[i+1] > 90) {
					q += r
					goto A
				}
				q += string(t[i])
			A:
			}
			t = q
			j++
		}
		for C(t, ")") {
			p := Index(t, ")")
			l := LastIndex(t[:p], "(")
			r := 1
			A := t[l+1] == 48
			T := t[l-1 : l]
			if T == "T" && !A ||
				T == "D" && (A || t[l+3] == 48) {
				r = 0
			}
			if T == "R" {
				if A && t[l+3] == 48 {
					r = 0
				}
				l++
			}
			t = t[:l-3] + Sprint(r) + t[p+1:]
		}
		a = "TRUE"
		if t == "0" {
			a = F
		}
		Println(a)
		n--
	}
}