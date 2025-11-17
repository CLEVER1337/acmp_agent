package main
import . "fmt"
func main() {
	var (
		n, x, y, i int
		a         = [100][100]int{{1}}
		j          = 1
	)
	
	Scan(&n)
	for j < n*n {
		if x < n-1 {
			x++
		} else if y < n-1 {
			y++
		}

		j++
		a[x][y] = j
		for x > 0 && y < n-1 {
			x--
			y++
			j++
			a[x][y] = j
		}
		y++
		if y == n {
			x++
			y--
		}
		j++
		a[x][y] = j
		for x < n-1 && y > 0 {
			x++
			y--
			j++
			a[x][y] = j
		}
	}

	for i < n {
		j = 0
		for j < n {
			Println(a[i][j])
			j++
		}
		i++
	}
}