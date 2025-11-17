package main
import . "fmt"
func main() {
	var (
		d, p                [251][251]int
		n, i, j, u, v, r, h int
		x                   = []int{-1, 1, 0, 0, 0, 0, -1, 1}
		a                   [251]string
		W                   = 99999
		P                   = Println
	)

	Scan(&n)
	for i < n {
		Scan(&a[i])
		j = 0
		for j < n {
			d[i][j] = W
			if a[i][j] == 64 {
				u = i
				v = j
			}
			if a[i][j] > 87 {
				r = i
				h = j
			}
			j++
		}
		i++
	}

	d[u][v] = 0
	q := [][2]int{{u, v}}

	for len(q) > 0 {
		i = q[0][0]
		j = q[0][1]
		q = q[1:]
		k := 0
		for k < 4 {
			u = i + x[k]
			v = j + x[k+4]
			if u >= 0 && u < n && v >= 0 && v < n && a[u][v] != 79 && d[u][v] > d[i][j]+1 {
				d[u][v] = d[i][j] + 1
				p[u][v] = k
				q = append(q, [2]int{u, v})
			}
			k++
		}
	}

	if d[r][h] < W {
		P("Y")
		for a[r][h] != 64 {
			a[r] = a[r][:h] + "+" + a[r][h+1:]
			v = p[r][h]
			r -= x[v]
			h -= x[v+4]
		}
		i = 0
		for i < n {
			P(a[i])
			i++
		}
	} else {
		P("N")
	}
}