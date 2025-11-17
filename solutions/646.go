package main
import . "fmt"
func main() {
	var (
		A, d             [1e4]int
		n, k, t, a, i, l int
	)
	d[0] = 1

	Scan(&n, &k)
	for i < n {
		Scan(&A[i])
		t += A[i]
		i++
	}

	for l < n {
		t = k
		for t > 0 {
			t--
			if t+A[l] < k {
				d[t+A[l]] += d[t]
			}
		}
		l++
	}

	for 0 < k {
		k--
		a += d[k]
	}

	t = 1<<n - 2*a
	if t < 0 {
		t = 0
	}

	Print(t)
}