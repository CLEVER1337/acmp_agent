
class Sphere:
    def __init__(self, mass, radius, x, y, z, vx, vy, vz):
        self.mass = mass
        self.radius = radius
        self.position = [x, y, z]
        self.velocity = [vx, vy, vz]

def parse_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        spheres = []
        for _ in range(n):
            mass, radius, x, y, z, vx, vy, vz = map(float, f.readline().split())
            spheres.append(Sphere(mass, radius, x, y, z, vx, vy, vz))
        T = int(f.readline())
    return spheres, T

def calculate_collisions(spheres):
    # Here you should implement the logic of sphere collisions
    pass

def write_output(filename, spheres):
    with open(filename, 'w') as f:
        for sphere in spheres:
            x, y, z = sphere.position
            vx, vy, vz = sphere.velocity
            f.write(f"{x} {y} {z} {vx} {vy} {vz}\n")

if __name__ == "__main__":
    spheres, T = parse_input("INPUT.TXT")
    calculate_collisions(spheres)  # This function is not implemented yet
    write_output("OUTPUT.TXT", spheres)
