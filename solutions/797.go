package main
import . "fmt"
type U = int
type A struct{ x, y, d, t U }
type S struct{}

var (
	q, w          [51]U
	i, b, c, x, y U
)

func F(x, y, b U) U {
	d := 0
	h := 0
	for h < b {
		f := h * 2
		if w[y] < 1 {
			d |= 3 << f
		}
		X := q[y]
		I := 1
		for I < 3 {
			if x <= X && X < x+b {
				d |= I << f
			}
			X = w[y]
			I++
		}
		y++
		h++
	}
	return d
}

func main() {
	Scan(&i, &b)

	for i := range q {
		q[i] = 51
	}

	for 0 < i {
		Scan(&x, &y)
		if x < q[y] {
			q[y] = x
		}
		if x > w[y] {
			w[y] = x
		}
		if y > c {
			c = y
		}
		i--
	}

	i = F(1, 1, b)
	d := map[U]S{i << 12: {}}
	u := []A{{1, 1, i, 0}}
	for len(u) > 0 {
		r := u[0]
		u = u[1:]
		if r.y > c-b && r.d == 1<<(b<<1)-1 {
			Print(r.t)
			break
		}
		for I, V := range []bool{
			r.x > 1,
			r.x < 51-b,
			r.y < 51-b && r.d&3 > 2} {
			if V {
				x = r.x - 1 + I&1*2 + I/2
				y = r.y + I/2
				C := r.d>>(I/2*2) | F(x, y, b)
				k := (x - 1) | (y-1)<<6 | C<<12
				_, V := d[k]
				if !V {
					d[k] = S{}
					u = append(u, A{x, y, C, r.t + 1})
				}
			}
		}
	}
}