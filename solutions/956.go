package main
import . "fmt"
func main() {
	var (
		z          [6]int
		w          []int
		n, i, o, p int
		s          = ""
		h          = s
		R          = 1 > 0
		M          = map[any]int{
			"A#": 1, "Bb": 1, "B": 2, "C": 3,
			"C#": 4, "Db": 4, "D": 5, "D#": 6,
			"Eb": 6, "E": 7, "F": 8, "F#": 9,
			"Gb": 9, "G": 10, "G#": 11, "Ab": 11}
		S = Scan
	)

	S(&n)
	for i < 6 {
		S(&s)
		z[i] = M[s]
		i++
	}

	S(&h)
	t := len(h)
	m := M[h]
	y := 0
	if t == 2 {
		m = M[h]
		y = 0
		if h[1] == 'm' || h[1] == 55 {
			m = M[h[:1]]
			y = 2 - int(h[1])/109
		}
	}
	if t > 2 {
		m = M[h[:2]]
		y = 0
		A := h[2] == 55
		B := h[2] == 'm'
		if A {
			y = 2
		}
		if B {
			y = 1
		}
		if B && A {
			m = M[h[:1]]
			y = 3
		}
		if t > 3 {
			y = 3
		}
	}

	q := map[int]bool{m: R}
	q[(m+4-y&1)%12] = R
	q[(m+7)%12] = R
	if y > 1 {
		q[(m+10)%12] = R
	}
	for v := range q {
		w = append(w, v)
	}

	n++
	for p < n {
		t = (z[0] + p) % 12
		if q[t] {
			f := 0
			for f < n {
				b := (z[1] + f) % 12
				if q[b] {
					l := 0
					for l < n {
						a := (z[2] + l) % 12
						if q[a] {
							r := 0
							for r < n {
								j := (z[3] + r) % 12
								if q[j] {
									i = 0
									for i < n {
										c := (z[4] + i) % 12
										if q[c] {
											x := 0
											for x < n {
												u := (z[5] + x) % 12
												if q[u] {
													k := 1
													for _, v := range w {
														if v != u && v != c && v != j && v != a && v != b && v != t {
															k = 0
														}
													}
													o += k
												}
												x++
											}
										}
										i++
									}
								}
								r++
							}
						}
						l++
					}
				}
				f++
			}
		}
		p++
	}

	Print(o)
}