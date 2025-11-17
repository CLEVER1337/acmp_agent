package main
import . "fmt"
func main() {
	a := 0
	i := 2
	b := ""
	Scan(&b, &a)
	for i < 37 {
		v := a
		c := ""
		for v > 0 {
			c = string("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[v%i]) + c
			v /= i
		}
		if b == c {
			Print(i)
			return
		}
		i++
	}

	Print(0)
}