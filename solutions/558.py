
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    radii = list(map(int, data[1:1+n]))
    radii.sort(reverse=True)
    
    count = 0
    for i in range(n):
        ri = radii[i]
        for j in range(i+1, n):
            rj = radii[j]
            for k in range(j+1, n):
                rk = radii[k]
                a = ri + rj
                b = ri + rk
                c = rj + rk
                if a <= b + c and b <= a + c and c <= a + b:
                    for l in range(k+1, n):
                        rl = radii[l]
                        if rl <= 0:
                            continue
                        s = (a + b + c) / 2.0
                        area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
                        r_inscribed = area_triangle / s
                        if r_inscribed >= rl:
                            count += 1
    print(count)

if __name__ == "__main__":
    main()
