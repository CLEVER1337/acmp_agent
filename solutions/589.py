
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        balls = []
        for i in range(n):
            data = list(map(float, f.readline().split()))
            balls.append({
                'mass': data[0],
                'radius': data[1],
                'pos': [data[2], data[3], data[4]],
                'vel': [data[5], data[6], data[7]],
                'index': i
            })
        T = float(f.readline().strip())
    return balls, T

def write_output(balls):
    with open('OUTPUT.TXT', 'w') as f:
        for ball in balls:
            f.write(f"{ball['pos'][0]:.3f} {ball['pos'][1]:.3f} {ball['pos'][2]:.3f} "
                   f"{ball['vel'][0]:.3f} {ball['vel'][1]:.3f} {ball['vel'][2]:.3f}\n")

def distance(ball1, ball2):
    return math.sqrt(sum((ball1['pos'][i] - ball2['pos'][i])**2 for i in range(3)))

def will_collide(ball1, ball2):
    r1, r2 = ball1['radius'], ball2['radius']
    pos1, pos2 = ball1['pos'], ball2['pos']
    vel1, vel2 = ball1['vel'], ball2['vel']
    
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    
    dvx = vel2[0] - vel1[0]
    dvy = vel2[1] - vel1[1]
    dvz = vel2[2] - vel1[2]
    
    a = dvx**2 + dvy**2 + dvz**2
    b = 2 * (dx * dvx + dy * dvy + dz * dvz)
    c = dx**2 + dy**2 + dz**2 - (r1 + r2)**2
    
    if a == 0:
        return float('inf')
    
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return float('inf')
    
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)
    
    if t1 >= 0:
        return t1
    elif t2 >= 0:
        return t2
    else:
        return float('inf')

def collide_balls(ball1, ball2):
    m1, m2 = ball1['mass'], ball2['mass']
    pos1, pos2 = ball1['pos'], ball2['pos']
    vel1, vel2 = ball1['vel'], ball2['vel']
    
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
    
    nx = dx / dist
    ny = dy / dist
    nz = dz / dist
    
    v1n = vel1[0] * nx + vel1[1] * ny + vel1[2] * nz
    v2n = vel2[0] * nx + vel2[1] * ny + vel2[2] * nz
    
    v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
    v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)
    
    dv1n = v1n_new - v1n
    dv2n = v2n_new - v2n
    
    ball1['vel'][0] += dv1n * nx
    ball1['vel'][1] += dv1n * ny
    ball1['vel'][2] += dv1n * nz
    
    ball2['vel'][0] += dv2n * nx
    ball2['vel'][1] += dv2n * ny
    ball2['vel'][2] += dv2n * nz

def simulate(balls, total_time):
    current_time = 0.0
    
    while current_time < total_time:
        next_collision_time = float('inf')
        colliding_pair = None
        
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                collision_time = will_collide(balls[i], balls[j])
                if collision_time < next_collision_time:
                    next_collision_time = collision_time
                    colliding_pair = (i, j)
        
        dt = min(total_time - current_time, next_collision_time)
        
        for ball in balls:
            for k in range(3):
                ball['pos'][k] += ball['vel'][k] * dt
        
        current_time += dt
        
        if current_time < total_time and colliding_pair:
            i, j = colliding_pair
            collide_balls(balls[i], balls[j])
    
    return balls

def main():
    balls, T = read_input()
    result = simulate(balls, T)
    write_output(result)

if __name__ == "__main__":
    main()
