package main
import . "fmt"
var e = []int{1, 1}
type A [2]int
func F(n int) int {
	for len(e) <= n {
		e = append(e, e[len(e)-1]+e[len(e)-2])
	}
	return e[n]
}
func T(v A) []A {
	q := A{1, 1}
	g := A{2, 2}
	if v == q {
		return []A{{1, 1}}
	}
	if v == g {
		return []A{{2, 2}, {1, 1}}
	}
	if v[1] <= F(v[0]-1) {
		r := T(A{v[0] - 1, v[1]})
		for i := range r {
			r[i][0]++
		}
		return append(r, q)
	}
	r := T(A{v[0] - 2, v[1] - F(v[0]-1)})
	for i := range r {
		r[i][0] += 2
		r[i][1] += F(v[0] - 1 - i)
	}
	return append(r, g, q)
}

func main() {
	l := 1
	g := 0

	Scan(&g)
	for F(l+2) < g+2 {
		l++
	}
	g -= F(l+1) - 2
	for _, o := range T(A{l, g}) {
		Println(F(o[0]+1) + o[1] - 2)
	}
}