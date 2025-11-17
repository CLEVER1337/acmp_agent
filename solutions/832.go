package main
import . "fmt"
func main() {
	n := 0
	Scan(&n)

	for i := 0; i < n; i++ {
		var A, B, C, z int
		P := Println
		Scan(&A, &B, &C)

		t := A + B + C

		if t == 0 {
			P("No")
			continue
		}
		if t == 1 {
			P("Yes")
			continue
		}

		if A > 0 {
			z++
		}
		if B > 0 {
			z++
		}
		if C > 0 {
			z++
		}

		if z < 2 {
			P("No")
			continue
		}

		t--
		o := (A & 1) + (B & 1) + (C & 1)
		s := "Yes"
		if t%2 == 0 {
			if o != 1 {
				s = "No"
			}
		} else if o != 2 {
			s = "No"
		}
		P(s)
	}
}