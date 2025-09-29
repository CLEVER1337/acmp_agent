
n, nAB, nBC, nAC = map(int, input().split())

if nAB + nBC + nAC > 2 * n:
    print("NO")
    exit(0)

kA = (nAB + nAC - nBC) // 2
kB = (nAB + nBC - nAC) // 2
kC = (nAC + nBC - nAB) // 2

if (nAB + nAC - nBC) % 2 != 0 or (nAB + nBC - nAC) % 2 != 0 or (nAC + nBC - nAB) % 2 != 0:
    print("NO")
    exit(0)

if kA < 0 or kB < 0 or kC < 0:
    print("NO")
    exit(0)

kAB = nAB - kA - kB
kBC = nBC - kB - kC
kAC = nAC - kA - kC

if kAB < 0 or kBC < 0 or kAC < 0:
    print("NO")
    exit(0)

if kA + kB + kC + kAB + kBC + kAC != n:
    print("NO")
    exit(0)

print("YES")
print(kA, kAB, kB, kBC, kC, kAC)
