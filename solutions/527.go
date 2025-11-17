package main
import . "fmt"
func main() {
	var a, b, c, d, t int
	Scan(&t)
	for 0 < t {
		Scan(&a, &b, &c, &d)
		g := "NO "
		if a == c && b == d {
			g = "YES "
		}
		for a > 0 && b > 0 {
			if a < b {
				a, b = b, a
			}
			if b == d && a >= c && (a-c)%b < 1 {
				g = "YES "
			}
			a %= b
		}
		Print(g)
		t--
	}
}