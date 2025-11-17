package main
import (
	. "fmt"
	. "math/big"
)

type R = Rat
type U struct{ X, Y *R }

var (
	f R
	P = Println
	N = NewRat
	o = N(2, 1)
)

func S(a, b *R) *R {
	r := f
	return r.Sub(a, b)
}
func A(a, b *R) *R {
	r := f
	return r.Add(a, b)
}
func L(a, b *R) *R {
	r := f
	return r.Mul(a, b)
}

func W(a, b U) U {
	var r, w R
	return U{r.Quo(A(a.X, b.X), o), w.Quo(A(a.Y, b.Y), o)}
}

func H(v U) U {
	r := f
	return U{r.Neg(v.Y), v.X}
}

func M(a, b, c U) (U, *R) {
	var t, k R
	q := W(a, b)
	w := H(U{S(b.X, a.X), S(b.Y, a.Y)})
	e := W(a, c)
	r := H(U{S(c.X, a.X), S(c.Y, a.Y)})
	t.Quo(A(
		A(L(e.X, w.Y), L(k.Neg(e.Y), w.X)),
		A(L(q.Y, w.X), L(new(R).Neg(q.X), w.Y))), S(L(r.Y, w.X), L(r.X, w.Y)))
	q = U{
		A(e.X, L(r.X, &t)),
		A(e.Y, L(r.Y, &t))}
	X := S(a.X, q.X)
	Y := S(a.Y, q.Y)
	return q, A(L(X, X), L(Y, Y))
}

func C(p, c U, h *R) bool {
	X, Y := S(p.X, c.X), S(p.Y, c.Y)
	return A(L(X, X), L(Y, Y)).Cmp(h) == 0
}

func main() {
	var n, k, y, i, j int64
	Scan(&n)
	s := make([]U, n)
	for j < n {
		Scan(&k, &y)
		s[j] = U{N(k, 1), N(y, 1)}
		j++
	}

	if n == 3 {
		P(`1 2
3`)
		return
	}
	if n == 4 {
		P(`1 2
3 4`)
		return
	}

	for i < 3 {
		j = i
		for j < 4 {
			j++
			k = j
			for k < 5 {
				k++
				z, h := M(s[i], s[j], s[k])
				var Z, H []int
				y = 0
				for l, v := range s {
					if C(v, z, h) {
						Z = append(Z, l+1)
					} else {
						H = append(H, l+1)
					}
				}
				if len(H) > 2 {
					o, p := M(s[H[0]-1], s[H[1]-1], s[H[2]-1])
					for _, v := range H {
						if !C(s[v-1], o, p) {
							goto A
						}
					}
				}
				for y < 2 {
					for _, x := range Z {
						Print(x, " ")
					}
					y++
					P()
					Z = H
				}
				return
			A:
			}
		}
		i++
	}
}