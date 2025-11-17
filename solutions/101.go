package main
import . "fmt"
var (
	o, z       [100]int
	u          []int
	n, k, a, I int
)

func F(i int) {
	e := k - len(u)
	if e < 1 {
		a++
		return
	}
	for i <= I-e {
		for _, v := range u {
			b := o[v] - o[i]
			if b < 0 {
				b = -b
			}
			d := z[v] - z[i]
			if d < 0 {
				d = -d
			}
			if o[v] == o[i] || z[v] == z[i] || b == d || b+d == 3 {
				goto A
			}
		}
		u = append(u, i)
		F(i + 1)
		u = u[:len(u)-1]
	A:
		i++
	}
}

func main() {
	Scan(&n, &k)
	i := 0
	for i < n {
		j := 0
		for j < n {
			o[I] = i
			z[I] = j
			I++
			j++
		}
		i++
	}

	F(0)
	Print(a)
}