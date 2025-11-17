package main
import . "fmt"
func main() {
	var (
		x, y       [100]int
		n, r, t, i int
	)

	Scan(&n)
	for t < n {
		Scan(&x[t], &y[t])
		t++
	}

	for i < n {
		j := i + 1
		for j < n {
			k := j + 1
			for k < n {
				X := []int{x[i], x[j], x[k]}
				Y := []int{y[i], y[j], y[k]}
				t = 0
				for t < 3 {
					A := (t + 1) % 3
					B := (t + 2) % 3
					if (X[A]-X[t])*(X[B]-X[t])+
						(Y[A]-Y[t])*(Y[B]-Y[t]) == 0 {
						a := X[A] + X[B] - X[t]
						b := Y[A] + Y[B] - Y[t]
						t = k + 1
						for t < n {
							if x[t] == a && y[t] == b {
								r++
							}
							t++
						}
					}
					t++
				}
				k++
			}
			j++
		}
		i++
	}

	Print(r)
}