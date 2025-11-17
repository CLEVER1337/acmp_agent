package main
import . "fmt"
func main() {
	n := 0
	k := 0

	Scan(&n, &k)
	i := n
	for {
		t := i
		j := 0
		for j < n {
			if t%n != k {
				break
			}
			t -= k + (t-k)/n
			if t < 1 {
				break
			}
			j++
			if j == n {
				Print(i)
				return
			}
		}
		i++
	}
}