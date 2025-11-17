package main
import (
	. "fmt"
	. "sort"
)

const N = 404

type T struct{ i, j, t, a, b, x, y, c, d int }

var (
	h, g, o, u [N]int
	q          [N * N]T
	p          [N * N]int
	U          [N][N]int
)

func G(a, b int) int {
	A := 0
	if a < b {
		A--
	}
	if a > b {
		A = 1
	}
	return A
}

func F(i, j int) int {
	for _, v := range []int{q[i].t - q[j].t,
		G(q[i].a, q[j].a), G(q[i].b, q[j].b)} {
		if v != 0 {
			return v
		}
	}
	if q[i].t != 0 {
		for _, v := range []int{
			G(q[i].x, q[j].x), G(q[i].y, q[j].y),
			G(q[i].c, q[j].c), G(q[i].d, q[j].d)} {
			if v != 0 {
				return v
			}
		}
	}
	return 0
}

func main() {
	var n, i, m, z, j, J int

	Scan(&n)
	for j < n {
		Scan(&g[j], &o[j], &h[j])
		j++
	}

	for i < n {
		j = 0
		for j < n {
			if i != j {
				var d T
				I := h[i]
				K := h[j]
				A := g[i]
				B := A + I
				Z := o[i]
				C := Z + I
				D := g[j]
				E := D + K
				H := o[j]
				L := H + K
				X := D <= A && E >= B
				Y := H <= Z && L >= C
				if X && Y {
					d = T{i, j, 0, 0, 0, 0, 0, 0, 0}
				} else if X && H > Z && H <= C && L >= C {
					d = T{i, j, 0, I, o[j] - o[i], 0, 0, 0, 0}
				} else if X && H <= Z && L >= Z && L < C {
					d = T{i, j, 0, I, o[i] + I - o[j] - K, 0, 0, 0, 0}
				} else if Y && D <= A && E >= A && E < B {
					d = T{i, j, 0, g[i] + I - g[j] - K, I, 0, 0, 0, 0}
				} else if Y && D > A && D <= B && E >= B {
					d = T{i, j, 0, g[j] - g[i], I, 0, 0, 0, 0}
				} else {
					if A > D {
						D = A
					}
					if Z > H {
						H = Z
					}
					if B < E {
						E = B
					}
					if C < L {
						L = C
					}
					D -= A
					E -= A
					B -= A
					H -= Z
					L -= Z
					C -= Z
					d = T{i, j, 0, I, I, 0, 0, 0, 0}
					if D >= 0 && D <= B && H >= 0 && H <= C && E-D > 0 && L-H > 0 {
						d = T{i, j, 1, B, C, D, H, E - D, L - H}
					}
				}
				q[m] = d
				p[m] = m
				m++
			}
			j++
		}
		i++
	}

	Slice(p[:m], func(i, j int) bool {
		return F(p[i], p[j]) < 0
	})

	for J < m {
		i = J
		for i < m && F(p[J], p[i]) == 0 {
			i++
		}
		n = J
		for n < i {
			l := q[p[n]].i
			L := q[p[n]].j
			z += n - J - u[l] - u[L] + U[L][l]
			u[l]++
			u[L]++
			U[l][L] = 1
			n++
		}
		n = J
		for n < i {
			l := q[p[n]].i
			L := q[p[n]].j
			u[l]--
			u[L]--
			U[l][L] = 0
			n++
		}
		J = i
	}

	Print(z * 2)
}