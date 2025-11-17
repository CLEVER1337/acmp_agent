package main
import . "fmt"
var m = map[int]int{}
func F(x int) int {
	if x < 4 {
		return x / 3
	}
	if v, o := m[x]
	o {
		return v
	}
	m[x] = F(x/2) + F((x+1)/2)
	return m[x]
}

func main() {
	a := 0
	Scan(&a)
	Print(F(a))
}