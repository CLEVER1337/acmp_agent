package main
import . "fmt"
func main() {
	k := 0
	m := 0
	i := 2

	Scan(&k)
	for i*i <= k {
		if k%i < 1 {
			if i > 2 && (m < 1 || i < m) {
				m = i
			}
			d := k / i
			if d > 2 && (m < 1 || d < m) {
				m = d
			}
		}
		i++
	}
	if m < 1 {
		m = k
		if m < 3 {
			m = 1
		}
	}
	Print(m - 1)
}