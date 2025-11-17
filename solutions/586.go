package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
func main() {
	var (
		a          [1e3][]int
		r          = b.NewReader(Stdin)
		i, q, w, z int
	)

	Scan(&q, &w, &z)
	for i < q {
		a[i] = make([]int, z+1)
		j := 0
		for j < z {
			j++
			n := 0
			for {
				b, _ := r.ReadByte()
				if b > 32 {
					for {
						n = n*10 + int(b-48)
						b, _ = r.ReadByte()
						if b < 48 || b > 57 {
							goto A
						}
					}
				}
			}
		A:
			a[i][n] = j
		}
		i++
	}

	i = z
	for z > 0 {
		k := 0
		j := 0
		for j < q {
			if a[j][z] < a[j][i] {
				k++
			}
			j++
		}
		if k >= w {
			i = z
		}
		z--
	}

	Print(i)
}