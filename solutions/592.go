package main
import (
	b "bufio"
	. "container/heap"
	. "fmt"
	o "os"
)

type U int32
type I = int
type B struct{ x, y, z, c, e U }
type P []B

func (p P) Len() I           { return len(p) }
func (p P) Less(i, j I) bool { return p[i].z+p[i].c < p[j].z+p[j].c }
func (p P) Swap(i, j I)      { p[i], p[j] = p[j], p[i] }
func (p *P) Push(x any)      { *p = append(*p, x.(B)) }
func (p *P) Pop() any {
	o := *p
	n := len(o) - 1
	m := o[n]
	*p = o[:n]
	return m
}

func main() {
	var (
		q          [1e4]P
		i, x, l, j I
		a, d       U
		p          P
		r          = b.NewReader(o.Stdin)
		S          = Fscan
	)

	S(r, &x)
	for i < x {
		S(r, &l)
		q[i] = make(P, l)
		j := 0
		for j < l {
			S(r, &a, &d)
			q[i][j].x = a
			q[i][j].y = d
			j++
		}
		Push(&p, B{x: U(i), z: q[i][0].x - 1})
		i++
	}

	for len(p) > 0 {
		e := Pop(&p).(B)
		i = I(e.x)
		if q[i][e.y].c < 1 {
			a = e.z + e.c
			s := [][]I{{i, I(e.y)}}
			for len(s) > 0 {
				l = len(s) - 1
				C := s[l][0]
				D := s[l][1]
				s = s[:l]
				q[C][D].c = 1
				q[C][D].z = a
				if D+1 < len(q[C]) {
					Push(&p, B{U(C), U(D + 1), q[C][D+1].x - q[C][D].y - 1, a, 0})
				}
				l = 0
				for l < 2 {
					Z := C + l*2 - 1
					if Z >= 0 && Z < x {
						b := q[C][D]
						o := 0
						w := len(q[Z])
						g := w
						for o < g {
							f := (o + g) / 2
							if q[Z][f].y < b.x {
								o = f + 1
							} else {
								g = f
							}
						}
						t := o
						o = 0
						g = w
						for o < g {
							f := (o + g) / 2
							if q[Z][f].x <= b.y {
								o = f + 1
							} else {
								g = f
							}
						}
						for t < o {
							if q[Z][t].c < 1 {
								s = append(s, []I{Z, t})
							}
							t++
						}
					}
					l++
				}
			}
		}
	}

	for j < x {
		i = len(q[j])
		a = 0
		if i > 0 {
			b := &q[j][i-1]
			a = b.y - b.z
		}
		Println(a)
		j++
	}
}