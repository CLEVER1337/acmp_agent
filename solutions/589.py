
import sys
import math

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    balls = []
    for i in range(1, n+1):
        parts = list(map(float, data[i].split()))
        ball = {
            'm': parts[0],
            'r': parts[1],
            'x': parts[2],
            'y': parts[3],
            'z': parts[4],
            'vx': parts[5],
            'vy': parts[6],
            'vz': parts[7],
            'id': i-1
        }
        balls.append(ball)
    
    T = float(data[-1].strip())
    
    current_time = 0.0
    while current_time < T:
        next_collision_time = float('inf')
        colliding_pair = None
        
        for i in range(n):
            for j in range(i+1, n):
                b1 = balls[i]
                b2 = balls[j]
                
                dx = b2['x'] - b1['x']
                dy = b2['y'] - b1['y']
                dz = b2['z'] - b1['z']
                dvx = b2['vx'] - b1['vx']
                dvy = b2['vy'] - b1['vy']
                dvz = b2['vz'] - b1['vz']
                
                a = dvx**2 + dvy**2 + dvz**2
                b = 2*(dx*dvx + dy*dvy + dz*dvz)
                c = dx**2 + dy**2 + dz**2 - (b1['r'] + b2['r'])**2
                
                if a == 0:
                    continue
                
                discriminant = b**2 - 4*a*c
                if discriminant < 0:
                    continue
                
                t1 = (-b - math.sqrt(discriminant)) / (2*a)
                t2 = (-b + math.sqrt(discriminant)) / (2*a)
                
                if t1 >= 0 and t1 < next_collision_time:
                    next_collision_time = t1
                    colliding_pair = (i, j)
                elif t2 >= 0 and t2 < next_collision_time:
                    next_collision_time = t2
                    colliding_pair = (i, j)
        
        if next_collision_time == float('inf') or current_time + next_collision_time > T:
            break
        
        dt = next_collision_time
        for ball in balls:
            ball['x'] += ball['vx'] * dt
            ball['y'] += ball['vy'] * dt
            ball['z'] += ball['vz'] * dt
        
        current_time += dt
        
        if colliding_pair:
            i, j = colliding_pair
            b1 = balls[i]
            b2 = balls[j]
            
            dx = b2['x'] - b1['x']
            dy = b2['y'] - b1['y']
            dz = b2['z'] - b1['z']
            dist = math.sqrt(dx**2 + dy**2 + dz**2)
            
            nx = dx / dist
            ny = dy / dist
            nz = dz / dist
            
            v1n = b1['vx'] * nx + b1['vy'] * ny + b1['vz'] * nz
            v2n = b2['vx'] * nx + b2['vy'] * ny + b2['vz'] * nz
            
            m1 = b1['m']
            m2 = b2['m']
            
            v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
            v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)
            
            dv1n = v1n_new - v1n
            dv2n = v2n_new - v2n
            
            b1['vx'] += dv1n * nx
            b1['vy'] += dv1n * ny
            b1['vz'] += dv1n * nz
            
            b2['vx'] += dv2n * nx
            b2['vy'] += dv2n * ny
            b2['vz'] += dv2n * nz
    
    remaining_time = T - current_time
    for ball in balls:
        ball['x'] += ball['vx'] * remaining_time
        ball['y'] += ball['vy'] * remaining_time
        ball['z'] += ball['vz'] * remaining_time
    
    for ball in balls:
        print("{:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}".format(
            ball['x'], ball['y'], ball['z'],
            ball['vx'], ball['vy'], ball['vz']
        ))

if __name__ == "__main__":
    main()
