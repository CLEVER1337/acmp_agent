package main
import (
	b "bufio"
	. "fmt"
	. "os"
)
var (
	C, q, H, O, d, w, A, B, Q, e, R, t, U [2e5 + 5]int
	y                                     = 0
	x                                     = 1
	P                                     = Println
)

func F(i, j, c, k int) {
	x++
	e[x] = j
	R[x] = k
	U[x] = c
	Q[x] = C[i]
	C[i] = x
}

func D(v, i int) {
	y++
	O[v] = y
	H[v] = y
	k := C[v]
	for k > 0 {
		j := e[k]
		if w[j]+B[k] > 1 && R[k] != i {
			if O[j] < 1 {
				D(j, R[k])
				if O[j] == H[j] {
					A[R[k]] = 1
				}
			}
			if H[j] < H[v] {
				H[v] = H[j]
			}
		}
		k = Q[k]
	}
}

func main() {
	r := b.NewReader(Stdin)
	var n, m, a, c, h, z, o, i, l, I, J, K, k int

	Scan(&n, &m)
	for k < m {
		Fscan(r, &z, &o, &i)
		z--
		o--
		F(z, o, i, k+1)
		F(o, z, i, k+1)
		k++
	}

	for l < n {
		l++
		d[l] = 9e9
	}

	z = 1
	for z < n {
		z <<= 1
	}
	i = z
	for i < z+n {
		t[i] = i - z
		i++
	}
	i = z + n
	for i < z+z {
		t[i] = n
		i++
	}
	i = z - 1
	for i > 0 {
		o = t[i*2]
		k = t[i*2+1]
		t[i] = k
		if d[o] < d[k] {
			t[i] = o
		}
		i--
	}

	for {
		i = t[1]
		if i == n || d[i] >= 9e9 {
			break
		}
		l = i + z
		t[l] = n
		l >>= 1
		for l > 0 {
			o = t[l*2]
			k = t[l*2+1]
			t[l] = k
			if d[o] < d[k] {
				t[l] = o
			}
			l >>= 1
		}
		g := C[i]
		for g != 0 {
			l = e[g]
			s := d[i] + U[g]
			if s < d[l] {
				d[l] = s
				v := (l + z) >> 1
				for v > 0 {
					o = t[v*2]
					k = t[v*2+1]
					t[v] = k
					if d[o] < d[k] {
						t[v] = o
					}
					v >>= 1
				}
			}
			g = Q[g]
		}
	}

	q[c] = n - 1
	c++
	w[n-1] = 1
	for h < c {
		i = q[h]
		h++
		z = C[i]
		for z != 0 {
			o = e[z]
			if w[o] < 1 && d[i] == d[o]+U[z] {
				w[o] = 1
				q[c] = o
				c++
			}
			z = Q[z]
		}
	}

	for I < n {
		z = C[I]
		for z != 0 {
			o = e[z]
			if w[I]+w[o] > 0 && d[I] == d[o]+U[z] {
				B[z] = 1
				B[z^1] = 1
			}
			z = Q[z]
		}
		I++
	}

	D(n-1, -1)

	for J < m {
		J++
		if A[J] > 0 {
			a++
		}
	}

	P(a)
	for K < m {
		K++
		if A[K] > 0 {
			P(K)
		}
	}
}