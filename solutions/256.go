package main
import . "fmt"
func main() {
	var x, y, z, n, p int
	a := ""
    
	Scan(&n)
	for 0 < n {
		Scan(&a, &p)
		if a == "X" {
			x += p
		}
		if a == "Y" {
			x += p
			z += p
		}
		if a == "Z" {
			z += p
		}
		n--
	}

	if x > 0 && z > 0 {
		y = x
		if y > z {
			y = z
		}
	}

	if x < 0 && z < 0 {
		q := -x
		if -z < q {
			q = -z
		}
		y = -q
	}

	x -= y
	z -= y

	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	if z < 0 {
		z = -z
	}
    
	Print(x + y + z)
}