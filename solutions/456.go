package main
import . "fmt"
func main() {
	var (
		f       = [21]int{0, 1, 1}
		x, y, b int
		z       = 2
	)

	Scan(&x, &y)
	for z < x {
		z++
		f[z] = f[z-2] + f[z-1]
	}

	z = f[x-2]
	for (y-f[x-1]*b)%z > 0 {
		b++
	}

	Print((y-f[x-1]*b)/z, b)
}