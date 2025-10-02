
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        balls = []
        for i in range(n):
            data = list(map(float, f.readline().split()))
            mi, ri, xi, yi, zi, vix, viy, viz = data
            balls.append({
                'mass': mi,
                'radius': ri,
                'pos': [xi, yi, zi],
                'vel': [vix, viy, viz]
            })
        T = float(f.readline().strip())
    
    current_time = 0.0
    
    while current_time < T:
        next_collision_time = float('inf')
        colliding_pair = None
        
        for i in range(n):
            for j in range(i + 1, n):
                ball1 = balls[i]
                ball2 = balls[j]
                
                dx = ball2['pos'][0] - ball1['pos'][0]
                dy = ball2['pos'][1] - ball1['pos'][1]
                dz = ball2['pos'][2] - ball1['pos'][2]
                
                dvx = ball2['vel'][0] - ball1['vel'][0]
                dvy = ball2['vel'][1] - ball1['vel'][1]
                dvz = ball2['vel'][2] - ball1['vel'][2]
                
                a = dvx**2 + dvy**2 + dvz**2
                b = 2 * (dx * dvx + dy * dvy + dz * dvz)
                c = dx**2 + dy**2 + dz**2 - (ball1['radius'] + ball2['radius'])**2
                
                if a == 0:
                    continue
                
                discriminant = b**2 - 4 * a * c
                if discriminant < 0:
                    continue
                
                t1 = (-b - math.sqrt(discriminant)) / (2 * a)
                t2 = (-b + math.sqrt(discriminant)) / (2 * a)
                
                if t1 >= 0 and t1 < next_collision_time:
                    next_collision_time = t1
                    colliding_pair = (i, j)
                elif t2 >= 0 and t2 < next_collision_time:
                    next_collision_time = t2
                    colliding_pair = (i, j)
        
        dt = min(next_collision_time, T - current_time)
        
        for i in range(n):
            ball = balls[i]
            ball['pos'][0] += ball['vel'][0] * dt
            ball['pos'][1] += ball['vel'][1] * dt
            ball['pos'][2] += ball['vel'][2] * dt
        
        current_time += dt
        
        if colliding_pair is not None and abs(current_time - T) < 1e-9:
            i, j = colliding_pair
            ball1 = balls[i]
            ball2 = balls[j]
            
            m1, m2 = ball1['mass'], ball2['mass']
            v1 = ball1['vel']
            v2 = ball2['vel']
            
            dx = ball2['pos'][0] - ball1['pos'][0]
            dy = ball2['pos'][1] - ball1['pos'][1]
            dz = ball2['pos'][2] - ball1['pos'][2]
            
            distance = math.sqrt(dx**2 + dy**2 + dz**2)
            nx = dx / distance
            ny = dy / distance
            nz = dz / distance
            
            v1n = v1[0] * nx + v1[1] * ny + v1[2] * nz
            v2n = v2[0] * nx + v2[1] * ny + v2[2] * nz
            
            v1n_new = ((m1 - m2) * v1n + 2 * m2 * v2n) / (m1 + m2)
            v2n_new = ((m2 - m1) * v2n + 2 * m1 * v1n) / (m1 + m2)
            
            dv1n = v1n_new - v1n
            dv2n = v2n_new - v2n
            
            ball1['vel'][0] += dv1n * nx
            ball1['vel'][1] += dv1n * ny
            ball1['vel'][2] += dv1n * nz
            
            ball2['vel'][0] += dv2n * nx
            ball2['vel'][1] += dv2n * ny
            ball2['vel'][2] += dv2n * nz
    
    with open('OUTPUT.TXT', 'w') as f:
        for ball in balls:
            f.write(f"{ball['pos'][0]:.3f} {ball['pos'][1]:.3f} {ball['pos'][2]:.3f} ")
            f.write(f"{ball['vel'][0]:.3f} {ball['vel'][1]:.3f} {ball['vel'][2]:.3f}\n")

if __name__ == "__main__":
    main()
