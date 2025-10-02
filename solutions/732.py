
n, nAB, nBC, nAC = map(int, input().split())

if n == 0:
    if nAB == 0 and nBC == 0 and nAC == 0:
        print("YES")
        print("0 0 0 0 0 0")
    else:
        print("NO")
else:
    # Угловые стулья считаются для двух стен
    # Обозначим: x = kA, y = kB, z = kC
    # Тогда: kAB = nAB - x - y >= 0
    #        kBC = nBC - y - z >= 0
    #        kAC = nAC - x - z >= 0
    #        x + y + z + kAB + kBC + kAC = n
    
    found = False
    for x in range(0, min(nAB, nAC) + 1):
        for y in range(0, min(nAB, nBC) + 1):
            for z in range(0, min(nBC, nAC) + 1):
                kAB = nAB - x - y
                kBC = nBC - y - z
                kAC = nAC - x - z
                
                if kAB >= 0 and kBC >= 0 and kAC >= 0:
                    total = x + y + z + kAB + kBC + kAC
                    if total == n:
                        print("YES")
                        print(f"{x} {kAB} {y} {kBC} {z} {kAC}")
                        found = True
                        break
            if found:
                break
        if found:
            break
            
    if not found:
        print("NO")
