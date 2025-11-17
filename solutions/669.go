package main
import . "fmt"
func main() {
	var (
		M, x, y, j, l, k, v int
		c                   [10]int
		i                   = 9
		P                   = Println
	)

	Scan(&M)
	for i > 1 {
		for M%i < 1 {
			M /= i
			c[i]++
		}
		i--
	}
	if M > 1 {
		P(-1, -1)
		return
	}
	i = 2
	for i < 10 {
		w := 0
		for w < c[i] {
			x = x*10 + i
			w++
		}
		i++
	}
	for j < c[7] {
		y = y*10 + 7
		j++
	}
	for l < c[5] {
		y = y*10 + 5
		l++
	}
	for k < c[3]+c[9]*2+c[6] {
		y = y*10 + 3
		k++
	}
	for v < c[2]+c[4]*2+c[6]+c[8]*3 {
		y = y*10 + 2
		v++
	}

	P(x, y)
}