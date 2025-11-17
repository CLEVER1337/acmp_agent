package main
import . "fmt"
var a [102][102]byte
func F(z, x, n int) {
	W := map[byte]byte{46: 47, 92: 88}
	V := map[byte]byte{46: 92, 47: 88}
	A := &a[z-1][x+1]
	B := &a[z-1][x]
	C := &a[z][x+1]
	D := &a[z-1][x-1]
	E := &a[z][x-1]
	G := &a[z+1][x+1]
	H := &a[z+1][x]
	J := &a[z+1][x-1]
	if n < 1 {
		if *B != 42 || *C != 42 {
			v, O := W[*A]
			if O {
				*A = v
				F(z-1, x+1, 0)
			}
		}
		if *A+*C < 85 {
			v, O := V[*B]
			if O {
				*B = v
				F(z-1, x, 1)
			}
		}
		if *A+*B < 85 {
			v, O := V[*C]
			if O {
				*C = v
				F(z, x+1, 2)
			}
		}
	}
	if n == 1 {
		if *B != 42 || *E != 42 {
			v, O := V[*D]
			if O {
				*D = v
				F(z-1, x-1, 1)
			}
		}
		if *D+*B < 85 {
			v, O := W[*E]
			if O {
				*E = v
				F(z, x-1, 3)
			}
		}
		if *D+*E < 85 {
			v, O := W[*B]
			if O {
				*B = v
				F(z-1, x, 0)
			}
		}
	}
	if n == 2 {
		if *H != 42 || *C != 42 {
			v, O := V[*G]
			if O {
				*G = v
				F(z+1, x+1, 2)
			}
		}
		if *G+*H < 85 {
			v, O := W[*C]
			if O {
				*C = v
				F(z, x+1, 0)
			}
		}
		if *G+*C < 85 {
			v, O := W[*H]
			if O {
				*H = v
				F(z+1, x, 3)
			}
		}
	}
	if n > 2 {
		if *H != 42 || *E != 42 {
			v, O := W[*J]
			if O {
				*J = v
				F(z+1, x-1, 3)
			}
		}
		if *J+*E < 85 {
			v, O := V[*H]
			if O {
				*H = v
				F(z+1, x, 2)
			}
		}
		if *J+*H < 85 {
			v, O := V[*E]
			if O {
				*E = v
				F(z, x-1, 1)
			}
		}
	}
}

func main() {
	var n, m, c, b, i, j, l int
	s := ""
	Scan(&n, &m)
	m++
	n++
	for i < 1+n {
		a[i][0] = 42
		a[i][m] = 42
		i++
	}
	for j < 1+m {
		a[0][j] = 42
		a[n][j] = 42
		j++
	}
	i = 1
	for i < n {
		Scan(&s)
		j = 1
		for j < m {
			a[i][j] = s[j-1]
			if a[i][j] == 88 {
				c = i
				b = j
			}
			j++
		}
		i++
	}

	for l < 4 {
		F(c, b, l)
		l++
	}

	i = 1
	for i < n {
		j = 1
		for j < m {
			Printf("%c", a[i][j])
			j++
		}
		Println()
		i++
	}
}