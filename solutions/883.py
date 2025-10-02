
n = int(input().strip())
circles = []
for i in range(n):
    r, c = map(int, input().split())
    circles.append((r, c, i))

circles.sort(key=lambda x: x[0], reverse=True)

coords = []
for i in range(n):
    r, c, idx = circles[i]
    if i == 0:
        coords.append((0.0, 0.0, idx))
    else:
        x = 0.0
        y = 0.0
        best_score = -10**18
        best_pos = (0.0, 0.0)
        
        for j in range(i):
            rx, ry, jdx = coords[j]
            rj, cj, _ = circles[j]
            dist = r + rj + 0.01
            
            for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
                rad = angle * 3.141592653589793 / 180.0
                nx = rx + dist * math.cos(rad)
                ny = ry + dist * math.sin(rad)
                
                if abs(nx) > 10000 or abs(ny) > 10000:
                    continue
                    
                score = 0
                for k in range(i):
                    cx, cy, kdx = coords[k]
                    rk, ck, _ = circles[k]
                    d = math.sqrt((nx - cx)**2 + (ny - cy)**2)
                    if d < r + rk:
                        score += ck
                
                if score > best_score:
                    best_score = score
                    best_pos = (nx, ny)
        
        coords.append((best_pos[0], best_pos[1], idx))

coords.sort(key=lambda x: x[2])
for x, y, idx in coords:
    print(f"{x:.10f} {y:.10f}")
