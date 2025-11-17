package main
import (
	d "bufio"
	. "fmt"
	. "os"
	. "strconv"
)
func main() {
	var (
		a, b, c             [2e3]int
		n, m, i, k, j, l, h int
		s                   = d.NewScanner(Stdin)
		S                   = Scan
		P                   = Print
	)
	s.Split(d.ScanWords)

	S(&n)
	for k < n {
		S(&a[k])
		k++
	}
	if n < 3 {
		i = a[0]
		if n > 1 {
			h = a[0]
			if h > a[1] {
				h = a[1]
			}
			i += a[1]
			for l < n {
				S(&a[l])
				l++
			}
			if h > a[0] {
				h = a[0]
			}
			if h > a[1] {
				h = a[1]
			}
			i += a[0] + a[1]
		}
		P(i - h)
		return
	}

	x := a[0] + a[1] + a[2]
	for j < n {
		S(&b[j])
		j++
	}
	for l < n-2 {
		m = b[l] + b[l+1] + b[l+2]
		if m > x {
			x = m
		}
		l++
	}

	j = 2
	for j < n {
		i = 0
		for i < n && s.Scan() {
			c[i], _ = Atoi(s.Text())
			i++
		}
		i = 0
		for i < n {
			m = a[i] + b[i] + c[i]
			if m > x {
				x = m
			}
			i++
		}
		i = 0
		for i < n-2 {
			m = c[i] + c[i+1] + c[i+2]
			if m > x {
				x = m
			}
			i++
		}
		i = 0
		for i < n-1 {
			q := c[i+1]
			g := b[i+1]
			for _, v := range [4]int{
				c[i] + q + g,
				b[i] + c[i] + q,
				b[i] + g + q,
				b[i] + g + c[i]} {
				if v > x {
					x = v
				}
			}
			i++
		}
		i = 0
		for i < n {
			a[i] = b[i]
			b[i] = c[i]
			i++
		}
		j++
	}
	P(x)
}