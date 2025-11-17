package main
import . "fmt"
func main() {
	var (
		q, w []string
		j    = 0
		m    = map[any]int{}
		s    = ""
	)

	for j < 2 {
		q, w = w, q
		i := 0
		Scan(&i)
		for 0 < i {
			Scan(&s)
			w = append(w, s)
			if j > 0 {
				m[s] = 0
			}
			i--
		}
		j++
	}

	for _, v := range q {
		j = len(v)
		i := 0
		for i < j {
			i++
			s = v[:i]
			o, e := m[s]
			if e && s == v[j-i:] {
				m[s] = o + 1
			}
		}
	}

	for _, s := range w {
		Println(m[s])
	}
}