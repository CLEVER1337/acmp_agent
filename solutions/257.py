
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        A, B, C, D = map(int, data)
    
    if A == 0 and B == 0 and C == 0:
        if D == 0:
            with open("OUTPUT.TXT", "w") as f:
                f.write("-1")
            return
        else:
            roots = []
    elif A == 0 and B == 0:
        if C != 0 and D % C == 0:
            roots = [-D // C]
        else:
            roots = []
    elif A == 0:
        discriminant = C * C - 4 * B * D
        if discriminant < 0:
            roots = []
        elif discriminant == 0:
            if C % (2 * B) == 0:
                roots = [-C // (2 * B)]
            else:
                roots = []
        else:
            root1 = (-C + discriminant**0.5) / (2 * B)
            root2 = (-C - discriminant**0.5) / (2 * B)
            roots = []
            if abs(root1 - round(root1)) < 1e-10:
                roots.append(int(round(root1)))
            if abs(root2 - round(root2)) < 1e-10:
                roots.append(int(round(root2)))
            roots = sorted(list(set(roots)))
    else:
        roots = []
        divisors_D = set()
        divisors_A = set()
        
        for i in range(1, int(abs(D))**0.5 + 1):
            if D != 0 and abs(D) % i == 0:
                divisors_D.add(i)
                divisors_D.add(-i)
                divisors_D.add(D // i)
                divisors_D.add(-D // i)
        
        for i in range(1, int(abs(A))**0.5 + 1):
            if A != 0 and abs(A) % i == 0:
                divisors_A.add(i)
                divisors_A.add(-i)
                divisors_A.add(A // i)
                divisors_A.add(-A // i)
        
        candidates = set()
        if D == 0:
            candidates.add(0)
        
        for p in divisors_D:
            for q in divisors_A:
                if q != 0 and p % q == 0:
                    candidate = p // q
                    candidates.add(candidate)
                    candidates.add(-candidate)
        
        for x in candidates:
            if A*x*x*x + B*x*x + C*x + D == 0:
                roots.append(x)
        
        roots = sorted(list(set(roots)))
    
    with open("OUTPUT.TXT", "w") as f:
        if len(roots) == 0:
            f.write("0")
        else:
            f.write(f"{len(roots)} " + " ".join(map(str, roots)))

if __name__ == "__main__":
    main()
