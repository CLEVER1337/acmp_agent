package main
import (
	. "fmt"
	. "math"
)

var (
	d, r, e, f, g, h, u, v, k, l float64
	m                            = 200
	o                            = 1e-8
)

func F(a, b float64) float64 {
	q := Abs(a - k)
	q = Min(q, Abs(a-2*Pi-k))
	q = Min(q, Abs(a+2*Pi-k))

	z := Abs(b - l)
	z = Min(z, Abs(b-2*Pi-l))
	z = Min(z, Abs(b+2*Pi-l))

	x := r * Cos(a)
	a = r * Sin(a)
	y := r * Cos(b)
	b = d + r*Sin(b)

	return Hypot((x-y), (a-b))/v + r*(q+z)/u
}

func main() {
	Scan(&d, &r, &e, &f, &g, &h, &u, &v)

	k = Acos(e / r)
	if f < 0 {
		k = -k
	}

	l = Acos(g / r)
	if h < d {
		l = -l
	}

	a := Pi / 9
	s := 1e9
	i := -Pi
	for i < Pi {
		j := -Pi
		for j < Pi {
			W := i
			R := i + a
			Y := 0.
			I := 0.
			Q := 1e9
			J := 0
			for Abs(W-R) > o && J < m {
				J++
				Y = W + (R-W)/3
				I = W + 2*(R-W)/3
				K := j
				Z := j + a
				A := 0.
				M := 0.
				L := 0
				for Abs(K-Z) > o && L < m {
					A = K + (Z-K)/3
					M = K + 2*(Z-K)/3
					if F(A, Y) > F(M, Y) {
						K = A
					} else {
						Z = M
					}
					L++
				}
				H := F(K, Y)
				K = j
				Z = j + a
				L = 0
				for Abs(K-Z) > o && L < m {
					A = K + (Z-K)/3
					M = K + 2*(Z-K)/3
					if F(A, I) > F(M, I) {
						K = A
					} else {
						Z = M
					}
					L++
				}
				D := F(K, I)
				if H > D {
					W = Y
					if D < Q {
						Q = D
					}
				} else {
					R = I
					if H < Q {
						Q = H
					}
				}
			}
			if Q < s {
				s = Q
			}
			j += a
		}
		i += a
	}

	Print(s)
}