package main

import . "fmt"

type Pos struct {
	ful, fur, fdl, fdr, lul, lur, ldl, ldr,
	bul, bur, bdl, bdr, rul, rur, rdl, rdr,
	uul, uur, udl, udr, dul, dur, ddl, ddr byte
}

func (p Pos) rotateFCW() Pos {
	a := p
	a.ful = p.fdl
	a.fur = p.ful
	a.fdr = p.fur
	a.fdl = p.fdr
	a.rul = p.udl
	a.dur = p.rul
	a.ldr = p.dur
	a.udl = p.ldr
	a.rdl = p.udr
	a.dul = p.rdl
	a.lur = p.dul
	a.udr = p.lur
	return a
}

func (p Pos) rotateFCCW() Pos {
	return p.rotateFCW().rotateFCW().rotateFCW()
}

func (p Pos) rotateLCW() Pos {
	a := p
	a.lul = p.ldl
	a.lur = p.lul
	a.ldr = p.lur
	a.ldl = p.ldr
	a.ful = p.uul
	a.dul = p.ful
	a.bdr = p.dul
	a.uul = p.bdr
	a.fdl = p.udl
	a.ddl = p.fdl
	a.bur = p.ddl
	a.udl = p.bur
	return a
}

func (p Pos) rotateLCCW() Pos {
	return p.rotateLCW().rotateLCW().rotateLCW()
}

func (p Pos) rotateBCW() Pos {
	a := p
	a.bul = p.bdl
	a.bur = p.bul
	a.bdr = p.bur
	a.bdl = p.bdr
	a.rur = p.ddr
	a.uul = p.rur
	a.ldl = p.uul
	a.ddr = p.ldl
	a.rdr = p.ddl
	a.uur = p.rdr
	a.lul = p.uur
	a.ddl = p.lul
	return a
}

func (p Pos) rotateBCCW() Pos {
	return p.rotateBCW().rotateBCW().rotateBCW()
}

func (p Pos) rotateRCW() Pos {
	a := p
	a.rul = p.rdl
	a.rur = p.rul
	a.rdr = p.rur
	a.rdl = p.rdr
	a.fur = p.dur
	a.uur = p.fur
	a.bdl = p.uur
	a.dur = p.bdl
	a.fdr = p.ddr
	a.udr = p.fdr
	a.bul = p.udr
	a.ddr = p.bul
	return a
}

func (p Pos) rotateRCCW() Pos {
	return p.rotateRCW().rotateRCW().rotateRCW()
}

func (p Pos) rotateUCW() Pos {
	a := p
	a.uul = p.udl
	a.uur = p.uul
	a.udr = p.uur
	a.udl = p.udr
	a.fur = p.rur
	a.lur = p.fur
	a.bur = p.lur
	a.rur = p.bur
	a.ful = p.rul
	a.lul = p.ful
	a.bul = p.lul
	a.rul = p.bul
	return a
}

func (p Pos) rotateUCCW() Pos {
	return p.rotateUCW().rotateUCW().rotateUCW()
}

func (p Pos) rotateDCW() Pos {
	a := p
	a.dul = p.ddl
	a.dur = p.dul
	a.ddr = p.dur
	a.ddl = p.ddr
	a.fdl = p.ldl
	a.rdl = p.fdl
	a.bdl = p.rdl
	a.ldl = p.bdl
	a.fdr = p.ldr
	a.rdr = p.fdr
	a.bdr = p.rdr
	a.ldr = p.bdr
	return a
}

func (p Pos) rotateDCCW() Pos {
	return p.rotateDCW().rotateDCW().rotateDCW()
}

func (p Pos) rotate(i int) Pos {
	if i == 0 {
		return p.rotateFCW()
	} else if i == 1 {
		return p.rotateFCCW()
	} else if i == 2 {
		return p.rotateLCW()
	} else if i == 3 {
		return p.rotateLCCW()
	} else if i == 4 {
		return p.rotateBCW()
	} else if i == 5 {
		return p.rotateBCCW()
	} else if i == 6 {
		return p.rotateRCW()
	} else if i == 7 {
		return p.rotateRCCW()
	} else if i == 8 {
		return p.rotateUCW()
	} else if i == 9 {
		return p.rotateUCCW()
	} else if i == 10 {
		return p.rotateDCW()
	} else if i == 11 {
		return p.rotateDCCW()
	} else {
		panic(1)
	}
}

func (left Pos) Less(right Pos) bool {
	if left.ful != right.ful {
		return left.ful < right.ful
	}
	if left.fur != right.fur {
		return left.fur < right.fur
	}
	if left.fdl != right.fdl {
		return left.fdl < right.fdl
	}
	if left.fdr != right.fdr {
		return left.fdr < right.fdr
	}
	if left.lul != right.lul {
		return left.lul < right.lul
	}
	if left.lur != right.lur {
		return left.lur < right.lur
	}
	if left.ldl != right.ldl {
		return left.ldl < right.ldl
	}
	if left.ldr != right.ldr {
		return left.ldr < right.ldr
	}
	if left.bul != right.bul {
		return left.bul < right.bul
	}
	if left.bur != right.bur {
		return left.bur < right.bur
	}
	if left.bdl != right.bdl {
		return left.bdl < right.bdl
	}
	if left.bdr != right.bdr {
		return left.bdr < right.bdr
	}
	if left.rul != right.rul {
		return left.rul < right.rul
	}
	if left.rur != right.rur {
		return left.rur < right.rur
	}
	if left.rdl != right.rdl {
		return left.rdl < right.rdl
	}
	if left.rdr != right.rdr {
		return left.rdr < right.rdr
	}
	if left.uul != right.uul {
		return left.uul < right.uul
	}
	if left.uur != right.uur {
		return left.uur < right.uur
	}
	if left.udl != right.udl {
		return left.udl < right.udl
	}
	if left.udr != right.udr {
		return left.udr < right.udr
	}
	if left.dul != right.dul {
		return left.dul < right.dul
	}
	if left.dur != right.dur {
		return left.dur < right.dur
	}
	if left.ddl != right.ddl {
		return left.ddl < right.ddl
	}
	if left.ddr != right.ddr {
		return left.ddr < right.ddr
	}
	return false
}

func (left Pos) Equal(right Pos) bool {
	return !left.Less(right) && !right.Less(left)
}

func main() {
	var (
		q    []Pos
		p    Pos
		from = map[Pos]Pos{}
	)
	Scanf("%c%c %c%c %c%c %c%c %c%c %c%c\n%c%c %c%c %c%c %c%c %c%c %c%c",
		&p.ful, &p.fur, &p.lul, &p.lur, &p.bul, &p.bur, &p.rul, &p.rur,
		&p.uul, &p.uur, &p.dul, &p.dur, &p.fdl, &p.fdr, &p.ldl, &p.ldr,
		&p.bdl, &p.bdr, &p.rdl, &p.rdr, &p.udl, &p.udr, &p.ddl, &p.ddr)

	from[p] = p
	q = append(q, p)
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		if u.ful == u.fur && u.fur == u.fdl && u.fdl == u.fdr &&
			u.lul == u.lur && u.lur == u.ldl && u.ldl == u.ldr &&
			u.bul == u.bur && u.bur == u.bdl && u.bdl == u.bdr &&
			u.rul == u.rur && u.rur == u.rdl && u.rdl == u.rdr &&
			u.uul == u.uur && u.uur == u.udl && u.udl == u.udr &&
			u.dul == u.dur && u.dur == u.ddl && u.ddl == u.ddr {
			if u.Equal(p) {
				Println("Solved")
				return
			}
			var res string
			prev := from[u]
			for u != p {
				for i := 0; i < 12; i++ {
					if prev.rotate(i).Equal(u) {
						S := ""
						switch i {
						case 0:
							S = "F"
						case 1:
							S = "F'"
						case 2:
							S = "L"
						case 3:
							S = "L'"
						case 4:
							S = "B"
						case 5:
							S = "B'"
						case 6:
							S = "R"
						case 7:
							S = "R'"
						case 8:
							S = "U"
						case 9:
							S = "U'"
						case 10:
							S = "D"
						case 11:
							S = "D'"
						}
						res = S + res
						break
					}
				}
				u = prev
				prev = from[u]
			}
			Print(res)
			return
		}
		for i := 0; i < 12; i++ {
			next := u.rotate(i)
			if _, e := from[next]; !e {
				from[next] = u
				q = append(q, next)
			}
		}
	}
}
