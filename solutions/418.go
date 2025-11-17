package main
import (
	b "bufio"
	. "container/list"
	. "fmt"
	. "os"
)
type B []byte
func main() {
	var (
		u    B
		r    = b.NewReader(Stdin)
		x    = 0
		e    = New()
		s, _ = r.ReadBytes('\n')
	)

	e.PushBack(B{})
	z := e.Front()

	for _, v := range s {
		if v > 31 {
			u = z.Value.(B)
			switch v {
			case 92:
				z = e.InsertAfter(B{}, z)
			case 60:
				k := len(u)
				if k > 0 {
					u = u[:k-1]
					z.Value = u
				} else if z != e.Front() {
					h := z.Prev()
					e.Remove(z)
					z = h
				}
			case 94:
				if z != e.Front() {
					z = z.Prev()
				}
			case 124:
				if z != e.Back() {
					z = z.Next()
				}
			default:
				u = append(u, v)
				z.Value = u
			}
			w := len(z.Value.(B))
			if w > x {
				x = w
			}
		}
	}

	Print(x)
}