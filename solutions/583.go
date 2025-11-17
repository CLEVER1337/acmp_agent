package main
import . "fmt"
func main() {
	var (
		d                []int
		a                [4e4]int
		q, n, x, y, h, B int
		A                = 114
		s                = "TRUE"
		F                = "FALSE"
		S                = Scan
	)

	S(&n)
	for h < n {
		s := ""
		S(&s)
		a[h] = int(s[0])
		if s[0] == 114 {
			x++
		}
		if s[0] == 108 {
			y++
		}
		if a[h] == 102 {
			S(&B)
		}
		h++
	}
	B = 108
	if y > x {
		A, B = B, A
	}
	for 0 < n {
		n--
		if a[n] == A {
			q++
			q %= 4
		} else if a[n] == B {
			q += 3
			q %= 4
		} else {
			d = append(d, q)
		}
	}
	for d[1] == 3 {
		d = append(d[2:], d[0], d[1])
	}
	x = len(d) - 1
	for d[x] == 1 {
		d = append([]int{d[x-1], d[x]}, d[:x-1]...)
	}
	h = 1
	for d[h+2] == 1 {
		h += 2
	}
	for d[x-2] == 3 {
		x -= 2
	}
	if h+2 != x {
		s = F
	}
	x = 2
	for x < h {
		if d[x] < 1 && n > 0 {
			s = F
		}
		n += d[x]
		x += 2
	}

	Print(s)
}