package main
import . "fmt"
func main() {
	var (
		s    = ""
		a    []int
		q    [2e3]int
		n, i int
	)

	Scan(&n)
	for i < n {
		Scan(&q[i])
		i++
		a = append(a, i)
	}

	i = n - 1
	for i >= 0 {
		o := len(a) - q[i] - 1
		s = Sprintln(a[o]) + s
		a = append(a[:o], a[o+1:]...)
		i--
	}

	Print(s)
}